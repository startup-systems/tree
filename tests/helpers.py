import os
import subprocess


def tree_correct(path):
    subprocess.run(['tree', path, '> /tmp/output.txt'])
    return open('output.txt').read()


def pytree(path):
    subprocess.run(['./pytree.py', path, '> /tmp/pytree.txt'])
    return open('pytree.txt').read()