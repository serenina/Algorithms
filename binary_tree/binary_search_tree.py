#!/usr/bin/env python/
class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def get_val(self):
        return self.val

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def insert_left(self, node):
        self.left = node
        node.parent = self

    def insert_right(self, node):
        self.right = node
        node.parent = self

    def is_left_child(self):
        return self.parent and self.parent.left == self

    def is_right_child(self):
        return self.parent and self.parent.right == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right or self.left)

    def has_any_children(self):
        return self.right or self.left

    def has_both_children(self):
        return self.right and self.left

    def replace_node_data(self, val, lc, rc):
        self.val = val
        self.left = lc
        self.right = rc
        if self.get_left_child():
            self.left.parent = self
        if self.get_right_child():
            self.right.parent = self


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

    def insert(self, val):
        if self.root:
            self.insert_node(TreeNode(val), self.root)
        else:
            self.root = TreeNode(val)

    def insert_node(self, new_node, current_node):
        if new_node.val <= current_node.val:
            if current_node.left:
                self.insert_node(new_node, current_node.left)
            else:
                current_node.insert_left(new_node)
        else:
            if current_node.get_right_child():
                self.insert_node(new_node, current_node.right)
            else:
                current_node.insert_right(new_node)

    def inorder(self):
        return self.print_inorder(self.root)

    def print_inorder(self, node):
        if self.length() == 1:
            print(self.root.get_val())
        elif self.length() == 0:
            print('empty tree')
        else:
            if node.get_left_child():
                self.print_inorder(node.get_left_child())
            print(node.get_val())
            if node.get_right_child():
                self.print_inorder(node.get_right_child())

    def preorder(self):
        return self.print_preorder(self.root)

    def print_preorder(self, node):
        if self.length() == 1:
            print(self.root.get_val())
        elif self.size == 0:
            print('empty tree')
        else:
            print(node.get_val())
            if node.get_left_child():
                self.print_preorder(node.get_left_child())
            if node.get_right_child():
                self.print_preorder(node.get_right_child())

    def search(self, val):
        return self.search_helper(self.root, val)

    def search_helper(self, node, val):
        if val == node.get_val():
            return node
        else:
            if val <= node.get_val():
                if node.get_left_child() is None:
                    print(val, 'not found')
                else:
                    return self.search_helper(node.get_left_child(), val)
            elif val > node.get_val():
                if node.get_right_child() is None:
                    print(val, 'not found')
                else:
                    return self.search_helper(node.get_right_child(), val)

    def tree_to_list(self, node):
        tree_list = [node.val]
        if node.left:
            tree_list += self.tree_to_list(node.left)
        if node.right:
            tree_list += self.tree_to_list(node.right)
        return tree_list

    def delete(self, node):
        if node.is_left_child():
            node.parent.left = None
        elif node.is_right_child():
            node.parent.right = None
        else:
            self.root = None
        if node.left:
            self.insert(node.left.val)
        if node.right:
            self.insert(node.right.val)

        node.parent = None
        node.left = None
        node.right = None


mytree = BinarySearchTree()

mytree.insert(10)
mytree.insert(5)
mytree.insert(11)
mytree.insert(12)
mytree.insert(3)
mytree.insert(10)
mytree.insert(6)

mytree.inorder()
#
mytree.delete(5)
#
print('new tree')
#
mytree.inorder()


# print(mytree.root.left.val)
# print(mytree.root.right.val)
