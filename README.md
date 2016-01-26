# Website Environment Generator
Python version: <code>2.7.10</code>

This is a very basic program to build website folder heirarchies automatically, to simplify the process of starting simple projects.

To run this script, navigate to the proper directory, and run <code>python web.py</code>

Certain libraries can be downloaded automatically; the full list is given below. For any library currently not supported,
an empty folder will be created in which you may place the files manually. Library files are downloaded from the owners of the libraries.

#### Currently supported libraries:
- React JS
- Bootstrap (CSS and JS)
- Isotope
- Angular

##### Adding more libraries
Adding further support is quite easy. All it takes currntly is an addition to the if statement that determines the library.
For example:
<pre>
def check_for_library_match(package):
    if package == "jquery":
        print("Downloading jQuery 1.12.0 from http://code.jquery.com/jquery-1.12.0.js...")
        return 'http://code.jquery.com/jquery-1.12.0.js'
    elif package == "isotope":
        print("Downloading isotopeJS 2.2.2 from cdnjs...")
        return 'http://cdnjs.cloudflare.com/ajax/libs/jquery.isotope/2.2.2/isotope.pkgd.min.js'
    else:
        return None
</pre>
The argument taken by <code>check_for_library</code> is a forced-lowercase string of whatever package is typed when prompted. Adding an all-lowercase condition as
an elif statement in the same format will allow more libraries to be downloaded. The logic will then format the URL for use once the
function returns.
For example:
<pre>
    elif package == "mylib":
      print("Downloading mylib 0.1 from far, far away...")
      return 'http://mylib.com/libraryfile/lib.js'
</pre>

#### File Generation
Once you are finished entering libraries, simply type <code>none</code> to end. At this point, 3 files will be generated:
- index.html
- site.js
- site.css

<code>index.html</code> will be automatically set up with HTML5 elements, and all the libraries are automatically added, inclduing
the automatically generated CSS and JS files.

##### Current workarounds
Certian packages (i.e. bootstrap and reactJS) require multiple files, and some CSS and JavaScript. For these, I have a second set of conditions that don't return anything and simply download the files and create directories directly.
<pre>
if package.lower() == "bootstrap":
    os.makedirs(projectname + "/assets/css/" + package)
    print("Downloading Bootstrap from maxcdn...")
    urllib.urlretrieve('https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css', projectname + '/assets/css/' + package + '/bootstrap.min.css')
    urllib.urlretrieve('https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js', projectname + '/assets/js/packages/' + package + '/bootstrap.min.js')
    css.append('/assets/css/' + package + '/bootstrap.min.css')
    scripts.append('/assets/js/packages/' + package + '/bootstrap.min.js')
</pre>

Changing the file location: The script will always navigate to your <code>/Docmuments/</code> folder. To change this, you can change
<code>folderlocation = 'Documents'</code> to something other than Documents, such as Desktop, Downloads, etc. Currently, these are the only directories that can be easily accessed.

#### Generated Heirarchy
The following is a sample heirarchy that could be generated:
<pre>
ProjectName
├── assets
│   ├── css
│   │   ├── bootstrap
│   │   │   └── bootstrap.min.css
│   │   └── site.css
│   ├── img
│   └── js
│       ├── packages
│       │   ├── bootstrap
│       │   │   └── bootstrap.min.js
│       │   └── jquery
│       │       └── jquery-1.12.0.js
│       └── site.js
└── index.html
</pre>

#### Deletion Script
Running <code>web-delete.py</code> will allow you to enter the names of directories in the <code>/Documents/</code> folder to delete. Note: this will, of course, allow you to delete any folder in the directory, not only ones created using <code>web.py</code>.  
