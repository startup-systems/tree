import os
import subprocess


def tree_correct(path):
    with open("/tmp/output.txt", "wb") as out, open("/tmp/err.txt", "wb") as err:
        subprocess.Popen(["tree",path], stdout=out, stderr=err)
    return open('/tmp/output.txt').read()


def pytree(path):
    with open("/tmp/pytree.txt", "wb") as out, open("/tmp/pyerr.txt", "wb") as err:
        subprocess.Popen(["./pytree.py",path], stdout=out, stderr=err)
    return open('/tmp/pytree.txt').read()

