#!/usr/bin/env python3
import sys,os
from collections import defaultdict

class Node(object):

    def __init__(self):
        self.name = ""
        self.metadata = {}
        self.children = []


class Tree(object):

    def __init__(self,root):
        """
        :param root: Root directory
        """
        self.root_node = Node()
        # Build the tree here
        pass

    def walk(self):
        """
        Walks starting from root and populates self.root_node
        :return:
        """
        pass

    def __str__(self):
        """
        Print the tree representations
        helpful hints https://en.wikipedia.org/wiki/Box-drawing_character
        :return:
        """
        return "Hello World"


def main(root,regex=None,collect_metadata=False):
    dir_tree = Tree(root)
    print(dir_tree)

if __name__ == '__main__':
    import os
    # main(sys.argv[1])
    # just for demo (NEVER EVER USE os.system like this, its a  security risk!)
    os.system('tree {}'.format(' '.join(sys.argv[1:])))