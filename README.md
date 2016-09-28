# Tree

> Tree is a recursive directory listing command that produces a depth indented listing of files

This assignment is to re-create the [`tree`](http://mama.indstate.edu/users/ice/tree/) command, using Python.

## Functionality

To play around with the actual `tree` command, you will need to install it within your [virtual machine](https://github.com/startup-systems/vm):

```bash
sudo apt update
sudo apt install tree
```

While the actual `tree` command accepts a bunch of optional flags/options, we are only going to worry about the basic use cases:

* Passing in a path as the first/only argument

    ```
    $ tree examples/simple/
    examples/simple/
    ├── another
    ├── bites
    │   ├── dust
    │   │   └── dot.jpg
    │   └── the
    └── one.txt

    2 directories, 4 files
    ```

* Not passing in any arguments, which will display the contents of the working directory

    ```
    $ cd examples/simple/
    $ tree
    .
    ├── another
    ├── bites
    │   ├── dust
    │   │   └── dot.jpg
    │   └── the
    └── one.txt

    2 directories, 4 files
    ```

Your script should produce identical output, but run with

```bash
python3 pytree.py [path]
```

## Requirements

* `pytest` tests passing (**100%** total)
* All of the logic must exist in Python. In other words, you may not use any of the following modules/functions:
    * `os.spawn*()`
    * `os.system()`
    * `subprocess`

## Running tests locally

Run the following from this directory:

```bash
# install dependencies
sudo apt update
sudo apt install tree
pip3 install -r requirements.txt
# run the tests
pytest -v
```
