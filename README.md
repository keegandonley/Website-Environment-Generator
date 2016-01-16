# Website Environment Generator
This is a very basic program to build website folder heirarchies automatically, to simplify the process of starting simple projects.

Certain libraries can be downloaded automatically; the full list is given below. For any library currently not supported, 
an empty folder will be created in which you may place the files manually. Library files are downloaded from the owners of the libraries.

#### Currently supported libraries:
- React JS 
- Bootstrap (CSS and JS)
- Isotope

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
