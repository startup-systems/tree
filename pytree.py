#!/usr/bin/env python3
import subprocess
import sys


class Node(object):

    def __init__(self):
        self.name = ""
        self.metadata = {}
        self.children = []


class Tree(object):

    def __init__(self, root):
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


def main(root, regex=None, collect_metadata=False):
    dir_tree = Tree(root)
    print(dir_tree)

if __name__ == '__main__':
    # just for demo
    subprocess.run(['tree'] + sys.argv[1:])
