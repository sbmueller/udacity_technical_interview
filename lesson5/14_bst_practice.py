#!/usr/bin/env python2

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_crawler(self.root, new_val)

    def insert_crawler(self, node, new_val):
        if node.value >= new_val:
            if node.left:
                self.insert_crawler(node.left, new_val)
            else:
                node.left = Node(new_val)
        if node.value < new_val:
            if node.right:
                self.insert_crawler(node.right, new_val)
            else:
                node.right = Node(new_val)

    def search(self, find_val):
        return self.search_crawler(self.root, find_val)

    def search_crawler(self, node, find_val):
        if node.value == find_val:
            return True
        if node.value >= find_val and node.left:
            return self.search_crawler(node.left, find_val)
        elif node.value < find_val and node.right:
            return self.search_crawler(node.right, find_val)
        return False

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
