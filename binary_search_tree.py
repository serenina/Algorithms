class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, val, lc, rc):
        self.val = val
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def insert(self, val):
        if self.root:
            self.insert_helper(val, self.root)
        else:
            self.root = TreeNode(val)

    def insert_helper(self, val, currentNode):
        if val <= currentNode:
            if currentNode.hasLeftChild():
                self.insert_helper(val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(val, parent = currentNode)
        else:
            if currentNode.hasRightChild():
                self.insert_helper(val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(val, parent = currentNode)

    def search(self, data):
        if self.root.val == data:
            return self.root
        elif:
            if data < self.root:
                return self.root.left.search(data)
            else:
                return self.root.right.search(data)
        else:
            print (data, 'not found')




    def delete(self, val):
        if self.root == val:
