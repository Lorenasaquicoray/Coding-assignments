class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.leftChild = None
        self.rightChild = None

class BinaryTree:
    def __init__(self):
        self.root = None

    #in order traversal from left, root , right
    def inorder(self, node):
        if node:
            self.inorder(node.leftChild)
            print(node.value, end=' ')
            self.inorder(node.rightChild)

    #root, left, right
    def preorder(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder(node.leftChild)
            self.preorder(node.rightChild)

    #left, right, root
    def postorder(self, node):
        if node:
            self.postorder(node.leftChild)
            self.postorder(node.rightChild)
            print(node.value, end=' ')

    # searching for a node with value k starting from node x
    # Iterative Tree Search: finds a node with value k starting from node x
    def iterative_tree_search(self, x, k):
        while x is not None and k != x.value:
            if k < x.value:  # If k is smaller, move to left subtree
                x = x.leftChild
            else:  # If k is larger, move to right subtree
                x = x.rightChild
        return x  # Returns the node if found, else None

    # Finds the minimum value node in the subtree rooted at 'node'
    def tree_minimum(self, node):
        while node.leftChild is not None:  # Go as left as possible
            node = node.leftChild
        return node  # Leftmost node is the minimum

    # Finds the inorder successor of a given node in a BST
    def tree_successor(self, myNode):
        if myNode.rightChild is not None:
            # If the node has a right subtree, successor is the leftmost node there
            return self.tree_minimum(myNode.rightChild)

        # Otherwise, go up the tree until you find a node that is a left child
        y = myNode.parent
        while y is not None and myNode == y.rightChild:
            myNode = y
            y = y.parent
        return y  # This is the lowest ancestor where the node is in the left subtree

    # Validates whether the tree rooted at 'node' is a Binary Search Tree (BST)
    def is_bst(self, node, min_val=float('-inf'), max_val=float('inf')):
        if node is None:
            return True  # An empty tree is a valid BST
        if not (min_val < node.value < max_val):  # Violates the BST property
            return False
        # Recursively check left and right subtrees with updated bounds
        return (self.is_bst(node.leftChild, min_val, node.value) and
                self.is_bst(node.rightChild, node.value, max_val))

# Driver code to test the tree functions
if __name__ == "__main__":
    tree = BinaryTree()
