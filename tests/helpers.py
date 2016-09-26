import os
import subprocess


def tree_correct(path):
    dest = '> correct_output.txt'
    subprocess.run(['tree', path, dest])
    return file('correct_output.txt').read()


def pytree(path):
    dest = '> pytree_output.txt'
    subprocess.run(['./pytree.py', path, dest])
    return file('pytree_output.txt').read()