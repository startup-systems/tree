# Tree

- Make sure tree command is installed, using apt; E.g. `sudo apt install tree`
- Implement tree command in python
- (Bonus) Collect extra metadata about each file and store it.
- (Bonus) Match file/foldernames based on some regular expression pattern, e.g. all *.jpeg files.

 Note: you cannot spawn a subprocess or shell, you must use os module. 
 For bonus regex matching must be done in python. 

Run `pytest` the tests should pass since it simply runs tree via python.

[![Build Status](https://travis-ci.org/startup-systems/tree.svg?branch=master)](https://travis-ci.org/startup-systems/tree)