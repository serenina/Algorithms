#!/usr/bin/env python

# import pytest
from binary_tree.binary_search_tree import BinarySearchTree, TreeNode


class TestBinarySearchTree(object):

    # def insert_str(self):
    #     b = BinarySearchTree()
    #     b.insert('b')
    #     expected_result = 'b'
    #     assert b.search('b') == expected_result

    def test_insert(self):
        b = BinarySearchTree()

        root = b.insert(TreeNode(10))
        assert b.root == root

        a = b.insert(TreeNode(5))
        assert b.root.left == a

        c = b.insert(TreeNode(11))
        assert b.root.right == c

        d = b.insert(TreeNode(12))
        assert d.parent == c

        b.insert(TreeNode(3))
        b.insert(TreeNode(10))
        b.insert(TreeNode(6))

    def test_test_tree_to_list(self):
        b = BinarySearchTree()
        b.insert(TreeNode(10))
        b.insert(TreeNode(5))
        b.insert(TreeNode(11))
        b.insert(TreeNode(12))
        b.insert(TreeNode(3))
        b.insert(TreeNode(10))
        b.insert(TreeNode(6))

        expected_result = [10, 5, 3, 10, 6, 11, 12]
        assert expected_result == b.tree_to_list(b.root)

    def test_remove_root(self):
        b = BinarySearchTree()

        root = b.insert(TreeNode(10))
        b.insert(TreeNode(5))
        b.insert(TreeNode(11))
        b.insert(TreeNode(12))
        b.insert(TreeNode(3))
        b.insert(TreeNode(10))
        b.insert(TreeNode(6))

        root_remove = b.delete(b.root)
        assert root == root_remove

        expected_result = [5, 3, 10, 6, 11, 12]
        assert b.tree_to_list(b.root) == expected_result

    def test_remove_internal_node(self):
        b = BinarySearchTree()
        b.insert(TreeNode(10))
        a = b.insert(TreeNode(5))
        b.insert(TreeNode(11))
        b.insert(TreeNode(12))
        b.insert(TreeNode(3))
        b.insert(TreeNode(10))
        b.insert(TreeNode(6))

        a_remove = b.delete(a)
        assert a == a_remove

        expected_result = [10, 3, 10, 6, 11, 12]
        assert b.tree_to_list(b.root) == expected_result
