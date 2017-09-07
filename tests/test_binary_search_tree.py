#!/usr/bin/env python

import pytest
from binary_tree.binary_search_tree import (BinarySearchTree,
                                            ValNotFoundException)


class TestBinarySearchTree(object):

    def test_insert_str(self):
        b = BinarySearchTree()
        b.insert_value('b')
        expected_result = 'b'

        assert b.search('b') == expected_result

    def test_search_value(self):
        b = BinarySearchTree()
        b.insert_value(10)
        b.insert_value(5)
        b.insert_value(11)
        b.insert_value(12)

        value_present = 10
        value_not_present = 42

        assert b.search(value_present) == value_present

        with pytest.raises(ValNotFoundException) as ex:
            b.search(value_not_present)
        assert ex.value.val == value_not_present

    def test_insert(self):
        b = BinarySearchTree()

        root = b.insert_value(10)
        assert b.root is root

        a = b.insert_value(5)
        assert b.root.left is a

        c = b.insert_value(11)
        assert b.root.right is c

        d = b.insert_value(12)
        assert d.parent is c

        b.insert_value(3)
        b.insert_value(10)
        b.insert_value(6)

    def test_tree_to_list(self):
        b = BinarySearchTree()
        b.insert_value(10)
        b.insert_value(5)
        b.insert_value(11)
        b.insert_value(12)
        b.insert_value(3)
        b.insert_value(10)
        b.insert_value(6)

        expected_result = [10, 5, 3, 10, 6, 11, 12]
        assert expected_result == b.tree_to_list(b.root)

    def test_remove_root(self):
        b = BinarySearchTree()

        root = b.insert_value(10)

        b.insert_value(5)
        b.insert_value(11)
        b.insert_value(12)
        b.insert_value(3)
        b.insert_value(10)
        b.insert_value(6)

        root_remove = b.delete(b.root)
        assert root is root_remove

        expected_result = [5, 3, 10, 6, 11, 12]
        assert b.tree_to_list(b.root) == expected_result

    def test_remove_internal_node(self):
        b = BinarySearchTree()

        b.insert_value(10)
        node_to_remove = b.insert_value(5)
        b.insert_value(11)
        b.insert_value(12)
        b.insert_value(3)
        b.insert_value(10)
        b.insert_value(6)

        node_to_remove_removed = b.delete(node_to_remove)
        assert node_to_remove is node_to_remove_removed

        expected_result = [10, 3, 10, 6, 11, 12]
        assert b.tree_to_list(b.root) == expected_result
