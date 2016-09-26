import os
import subprocess


def tree_correct(path):
    dest = '> tree_output.txt'
    subprocess.run(['tree', path, dest])
    return open('tree_output.txt').read()


def pytree(path):
    dest = '> pytree_output.txt'
    subprocess.run(['./pytree.py', path, dest])
    return open('pytree_output.txt').read()