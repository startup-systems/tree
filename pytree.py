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
        Walks starting from root and populates self.tree
        :return:
        """
        pass

    def __str__(self):
        """
        Print the tree representations
        :return:
        """
        pass


def main(root,regex=None,collect_metadata=False):
    dir_tree = Tree(root)

if __name__ == '__main__':
    pass