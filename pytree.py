#!/usr/bin/env python3
import subprocess
import sys


# YOUR CODE GOES here


if __name__ == '__main__':
    # just for demo
    subprocess.run(['tree'] + sys.argv[1:])
