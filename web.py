"""
Script to generate a folder heirarchy used for web design
Author: Keegan Donley
"""
import os
import urllib


def main():
    projectname = raw_input("Enter your project name: ")
    while len(projectname) <= 0:
        print("Please enter a valid project name!")
        projectname = raw_input("Enter your project name: ")
    folderlocation = 'Documents'
    rootdir = get_root_dir
    while rootdir != os.getcwd():
        os.chdir(os.pardir)
        rootdir = get_root_dir()

    os.chdir(folderlocation)
    os.makedirs(projectname + "/assets/js/")
    os.makedirs(projectname + "/assets/css/")
    os.makedirs(projectname + "/assets/img/")
    package = raw_input("Enter a package name to add, or none: ")
    scripts = []
    css = []
    while package.lower() != "none":
        if len(package) > 0:
            os.makedirs(projectname + "/assets/js/packages/" + package)
            if package.lower() == "bootstrap":
                os.makedirs(projectname + "/assets/css/" + package)
                print("Downloading Bootstrap from maxcdn...")
                urllib.urlretrieve('https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css', projectname + '/assets/css/' + package + '/bootstrap.min.css')
                urllib.urlretrieve('https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js', projectname + '/assets/js/packages/' + package + '/bootstrap.min.js')
                css.append('assets/css/' + package + '/bootstrap.min.css')
                scripts.append('assets/js/packages/' + package + '/bootstrap.min.js')
            if package.lower() == "react":
                print("Downloading react and react dom 0.14.6 from fb.me...")
                urllib.urlretrieve('https://fb.me/react-with-addons-0.14.6.js', projectname + '/assets/js/packages/' + package + '/react-with-addons-0.14.6.js')
                urllib.urlretrieve('https://fb.me/react-dom-0.14.6.js', projectname + '/assets/js/packages/' + package + '/react-dom-0.14.6.js')
                scripts.append('assets/js/packages/' + package + '/react-with-addons-0.14.6.js')
                scripts.append('assets/js/packages/' + package + '/react-dom-0.14.6.js')
            librarymatch = check_for_library_match(package.lower())
            if librarymatch != None:
                url = librarymatch.split('/')
                filename = url[-1]
                urllib.urlretrieve(librarymatch, projectname + '/assets/js/packages/' + package + '/' + filename)
                scripts.append('assets/js/packages/' + package + '/' + filename)
            elif librarymatch == None and package.lower() != "bootstrap" and package.lower() != "react":
                print("No file found to download... Don't forget to manually add the files needed.")
        else:
            print("Please enter none or a valid string!")
        package = raw_input("Enter a package name to add, or none: ")
    create_files(projectname, scripts, css)
    os.chdir(os.pardir)
    os.chdir(os.pardir)
    print("Project successfully created at: " + os.getcwd())


def get_root_dir():
    currentdir = os.getcwd()
    currentdir = currentdir.split('/')
    rootdir = '/' + currentdir[1] + '/' + currentdir[2]
    return rootdir


def check_for_library_match(package):
    # TODO: load these names and urls from an external file
    if package == "jquery":
        print("Downloading jQuery 1.12.0 from http://code.jquery.com/jquery-1.12.0.js...")
        return 'http://code.jquery.com/jquery-1.12.0.js'
    elif package == "isotope":
        print("Downloading isotopeJS 2.2.2 from cdnjs...")
        return 'http://cdnjs.cloudflare.com/ajax/libs/jquery.isotope/2.2.2/isotope.pkgd.min.js'
    else:
        return None


def create_files(projectname, scripts, css):
    os.chdir(projectname)
    htmlFile = open("index.html", "w")
    htmlFile.write("<!DOCTYPE html>\n<html>\n<head>\n")
    htmlFile.write("    <title>" + projectname + "</title>\n\n")
    htmlFile.write("    <script src='assets/js/site.js'></script>\n")
    for i in range(len(scripts)):
        htmlFile.write("    <script src='" + scripts[i] + "'></script>\n")
    for i in range(len(css)):
        htmlFile.write("    <link rel='stylesheet' href='" + css[i] + "'>\n")
    htmlFile.write("    <link rel='stylesheet' href='assets/css/site.css'>\n")
    htmlFile.write("</head>\n<body>\n\n</body>\n</html>")
    htmlFile.close()
    create_js_file()


def create_js_file():
    os.chdir("assets")
    os.chdir("js")
    jsFile = open("site.js", "w")
    jsFile.close()
    create_css_file()


def create_css_file():
    os.chdir(os.pardir)
    os.chdir("css")
    cssFile = open("site.css", "w")
    cssFile.write("// auto generated CSS file, automatically added to index.html")
    cssFile.close()


main()
