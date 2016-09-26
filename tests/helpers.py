import os
import subprocess


def tree_correct(path):
    subprocess.run(['tree', path, '> output.txt'])
    return open('output.txt').read()


def pytree(path):
    subprocess.run(['./pytree.py', path, '> pytree.txt'])
    return open('pytree.txt').read()