#!/usr/bin/env python/
class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def insert_left(self, new_node):
        self.left = new_node
        new_node.parent = self

    def insert_right(self, new_node):
        self.right = new_node
        new_node.parent = self


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0
        self.tree_list = []

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def insert(self, new_node, current_node=None):
        if self.root is None:
            self.root = new_node
            return self.root

        if current_node is None:
            current_node = self.root

        if new_node.val <= current_node.val:
            if current_node.left:
                self.insert(new_node, current_node.left)
            else:
                current_node.insert_left(new_node)
        else:
            if current_node.right:
                self.insert(new_node, current_node.right)
            else:
                current_node.insert_right(new_node)

        return new_node

    def inorder(self):
        return self.print_inorder(self.root)

    def print_inorder(self, new_node):
        if new_node.left:
            self.print_inorder(new_node.left)
        print(new_node.get_val())
        if new_node.right:
            self.print_inorder(new_node.right)

    def preorder(self):
        return self.print_preorder(self.root)

    def print_preorder(self, node):
        print(node.get_val())
        if node.left:
            self.print_preorder(node.left)
        if node.right:
            self.print_preorder(node.right)

    def tree_to_list(self, node):
        tree_list = [node.val]
        if node.left:
            tree_list += self.tree_to_list(node.left)
        if node.right:
            tree_list += self.tree_to_list(node.right)
        return tree_list

    def search(self, val):
        return self.search_helper(self.root, val)

    def search_helper(self, node, val):
        if val == node.get_val():
            return node
        else:
            if val <= node.get_val():
                if node.left is None:
                    print(val, 'not found')
                else:
                    return self.search_helper(node.left, val)
            elif val > node.get_val():
                if node.right is None:
                    print(val, 'not found')
                else:
                    return self.search_helper(node.right, val)

    def delete(self, node):
        if node.parent is None:
            self.root = None
        else:
            if node.parent.left == node:
                node.parent.left = None
            elif node.parent.right == node:
                node.parent.right = None

        if node.left:
            self.insert(node.left)

        if node.right:
            self.insert(node.right)

        node.parent = None
        node.left = None
        node.right = None

        return node
