"""
Script to generate a folder heirarchy used for web design
Author: Keegan Donley
"""
import os
import urllib
import shutil

# The colors used for highlighting text output
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    LOG = '\033[90m'
    ENDC = '\033[0m'


def main():
    print_welcome()
    projectname = raw_input("Enter your project name: ")
    while len(projectname) <= 0:
        print(colors.FAIL + "Please enter a valid project name!" + colors.ENDC)
        projectname = raw_input("Enter your project name: ")
    folderlocation = 'Documents'
    rootdir = get_root_dir

    # Set the working directory to /Users/<username>/Documents
    # Only works currently if the script is run from a folder located below /Users/<username>/
    while rootdir != os.getcwd():
        os.chdir(os.pardir)
        rootdir = get_root_dir()

    os.chdir(folderlocation)
    os.makedirs(projectname + "/assets/js/")
    os.makedirs(projectname + "/assets/css/")
    os.makedirs(projectname + "/assets/img/")

    # Attempt to set up the basic folder heirarchy
    # Loop to input all packages the user desires, and download the package if supported
    package = raw_input("Enter a package name to add, 'none' to finish, or 'help': ")
    scripts = []
    css = []
    while package.lower() != "none":
        if len(package) > 0 and package.lower() != "help" and package.lower() != "h":
            os.makedirs(projectname + "/assets/js/packages/" + package)

            # Bootstrap needs a special method of installation in order to place files in both
            # CSS and JS folders
            if package.lower() == "bootstrap":
                os.makedirs(projectname + "/assets/css/" + package)
                print(colors.LOG + "Downloading Bootstrap from maxcdn..." + colors.ENDC)
                urllib.urlretrieve('https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css', projectname + '/assets/css/' + package + '/bootstrap.min.css')
                urllib.urlretrieve('https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js', projectname + '/assets/js/packages/' + package + '/bootstrap.min.js')
                css.append('assets/css/' + package + '/bootstrap.min.css')
                scripts.append('assets/js/packages/' + package + '/bootstrap.min.js')
            # React behaves the same way as bootstrap, with 2 JS files
            if package.lower() == "react":
                print(colors.LOG + "Downloading react and react dom 0.14.6 from fb.me..." + colors.ENDC)
                urllib.urlretrieve('https://fb.me/react-with-addons-0.14.6.js', projectname + '/assets/js/packages/' + package + '/react-with-addons-0.14.6.js')
                urllib.urlretrieve('https://fb.me/react-dom-0.14.6.js', projectname + '/assets/js/packages/' + package + '/react-dom-0.14.6.js')
                scripts.append('assets/js/packages/' + package + '/react-with-addons-0.14.6.js')
                scripts.append('assets/js/packages/' + package + '/react-dom-0.14.6.js')

            # Check if the entered package matches one of the stored libraries
            librarymatch = check_for_library_match(package.lower())
            if librarymatch != None:
                # Separate out the filename
                url = librarymatch.split('/')
                filename = url[-1]
                urllib.urlretrieve(librarymatch, projectname + '/assets/js/packages/' + package + '/' + filename)
                scripts.append('assets/js/packages/' + package + '/' + filename)
            elif librarymatch == None and package.lower() != "bootstrap" and package.lower() != "react":
                print(colors.WARNING + "No file found to download... Don't forget to manually add the files needed." + colors.ENDC)
        elif package.lower() == "help" or package.lower() == "h":
            display_help(projectname)
        else:
            print(colors.FAIL + "Please enter 'none' or a valid string!" + colors.ENDC)
        package = raw_input("Enter a package name to add, 'none' to finish, or 'help': ")
    create_files(projectname, scripts, css)
    os.chdir(os.pardir)
    os.chdir(os.pardir)
    save_setup(projectname)


def get_root_dir():
    '''
    This function determines the root directory to change the working directory to.
    returns: string of the root directory, in the format /Users/<username>/
    '''
    currentdir = os.getcwd()
    currentdir = currentdir.split('/')
    rootdir = '/' + currentdir[1] + '/' + currentdir[2]
    return rootdir


def check_for_library_match(package):
    '''
    This function checks if the package entered by the user matches one with a download link.
    parameter: package (string): the string the user entered when prompted for a library to add (forced-lowercase)
    returns: string: the URL to download, or None if no match is found
    '''
    # TODO: load these names and urls from an external file
    if package == "jquery":
        print(colors.LOG + "Downloading jQuery 1.12.0 from http://code.jquery.com/jquery-1.12.0.js..." + colors.ENDC)
        return 'http://code.jquery.com/jquery-1.12.0.js'
    elif package == "isotope":
        print(colors.LOG + "Downloading isotopeJS 2.2.2 from cdnjs..." + colors.ENDC)
        return 'http://cdnjs.cloudflare.com/ajax/libs/jquery.isotope/2.2.2/isotope.pkgd.min.js'
    elif package == "angular":
        print(colors.LOG + "Downloading AngularJS 1.4.8 from googleapis.com..." + colors.ENDC)
        return("https://ajax.googleapis.com/ajax/libs/angularjs/1.4.8/angular.min.js")
    else:
        return None


def create_files(projectname, scripts, css):
    '''
    This function generates the HTML, CSS, and JS files for use by the user.
    parameter: projectname (string): the name of the project entered by the user
    parameter: scripts (list): the list of all scripts needed to be linked
    parameter: css (list): the list of all css files entered
    '''
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
    '''
    Creates an empty JS file for use by the user. Called by create_files().
    '''
    os.chdir("assets")
    os.chdir("js")
    jsFile = open("site.js", "w")
    jsFile.close()
    create_css_file()


def create_css_file():
    '''
    Creates a CSS file for use by the user. Called by create_css_file().
    '''
    os.chdir(os.pardir)
    os.chdir("css")
    cssFile = open("site.css", "w")
    cssFile.write("// auto generated CSS file, automatically added to index.html")
    cssFile.close()


def display_help(projectname):
    '''
    Displays the help screen when the user requests it.
    parameter: projectname (string): the name of the project entered by the user
    '''
    os.system('clear')
    print("Project Name: " + projectname)
    print("\n---------------------- Help ----------------------")
    print("Type the name of the library you wish to install")
    print("Currently supported libraries:")
    print(" * jQuery")
    print(" * Bootstrap")
    print(" * React")
    print(" * Isotope")
    print(" * Angular")
    print("Currently, dependencies aren't taken into account for,")
    print("so jQuery must be installed first if it is needed by any")
    print("other libraries.\n")
    print("If you add a module that is not yet supported, a folder")
    print("will be created with the correct name. Don't forget after")
    print("everything is generated to manually add the libarary")
    print("files you need.")
    print("--------------------------------------------------\n")

    page2 = raw_input("Type next for more help, or anything else to return: ")
    if page2.lower() == 'next':
        os.system('clear')
        print("Project Name: " + projectname)
        print("\n------------------ Help Page 2 -------------------")
        print("This program will generate an HTML file, JS file, and")
        print("CSS file.")
        print("\nIf you use a supported library, these files will be")
        print("generated automatically with external scripts linked,")
        print("but if the library isn't supported, you'll need to")
        print("manually link them after the script is finished.")
        print("\nFor testing purposes, when the script is done, you'll")
        print("have the option to save or delete the confiuration")
        print("you just created")
        print("--------------------------------------------------\n")
    else:
        os.system('clear')
        print("Project Name: " + projectname)


def print_welcome():
    '''
    Print the welcome screen for the user.
    '''
    os.system('clear')
    print(colors.OKBLUE + "------------- Web Heirarchy Generator ------------")
    print("By Keegan Donley\n")
    print("Please begin by entering the desired name of your")
    print("new site's root directory.")
    print("--------------------------------------------------\n" + colors.ENDC)

def save_setup(projectname):
    '''
    Prompts to save or delete the current configuration.
    parameter: projectname (string): the name of the project entered by the user
    '''
    os.system('clear')
    print("\nAlmost done!")
    save = raw_input("Type yes to save your work, or no to discard this configuration: ")
    while save != "yes" and save != "no":
        print("Please enter yes or no!")
        save = raw_input("Type yes to save your work, or no to discard this configuration: ")
    if save.lower() == "yes" or save.lower() == "y":
        os.system('clear')
        print(colors.OKGREEN + "\nProject successfully created at: " + os.getcwd() + "\n" + colors.ENDC)
    elif save.lower() == "no" or save.lower() == "n":
        print(colors.FAIL + "\n--------------------------------------------------------" + colors.ENDC)
        print(colors.FAIL + "WARNING! You're about to discard your current work" + colors.ENDC)
        print(colors.FAIL + "--------------------------------------------------------\n" + colors.ENDC)
        confirmation = raw_input("Please type deletedelete in order to confirm: ")
        if confirmation.lower() == "deletedelete":
            os.chdir(os.pardir)
            shutil.rmtree(projectname)
            os.system('clear')
            print(colors.OKGREEN + "\nProject " + projectname + " successfully deleted\n" + colors.ENDC)
        else:
            print(colors.WARNING + "\nConfirmation phrase incorrect." + colors.ENDC)
            print(colors.OKGREEN + "Project successfully created at: " + os.getcwd() + colors.ENDC)

main()
