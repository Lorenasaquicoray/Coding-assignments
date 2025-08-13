RED = "RED"
BLACK = "BLACK"

class Node:
    def __init__(self, key, color, left =None, right =None, parent = None ):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent


class RedBlackTree:
    def __init__(self):
        self.T_nil = Node(None, BLACK)
        self.root = self.T_nil

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.T_nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.T_nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y


    def right_rotate(self, x):
        y = x.left
        x.left = y.right

        if y.right != self.T_nil:
            y.right.parent = x

        y.parent = x.parent

        if x.parent == self.T_nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def rbinsert(self, key):
        z = Node(key, RED, left=self.T_nil, right=self.T_nil)
        y = self.T_nil
        x = self.root

        while x != self.T_nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y

        if y == self.T_nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        self.rbinsertfixup(z)

    def rbinsertfixup(self, z):
        while z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.left_rotate(z.parent.parent)

        self.root.color = BLACK

    def rbtransplant(self, u, v):
        if u.parent == self.T_nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def inorder_print(self, node): #in order left root right
        if node != self.T_nil:
            self.inorder_print(node.left)
            print(f"{node.key} ({node.color})", end=' ')
            self.inorder_print(node.right)

    def print_tree(self):
        self.inorder_print(self.root)
        print()


    def print_helper(self, node, indent="", last=True):
        if node != self.T_nil:
            print(indent, end='')
            if last:
                print("R----", end='')
                indent += "     "
            else:
                print("L----", end='')
                indent += "|    "
            print(f"{node.key}({node.color})")
            self.print_helper(node.left, indent, False)
            self.print_helper(node.right, indent, True)


    def drawtree(self):
        self.print_helper(self.root)

if __name__ == "__main__":
    tree = RedBlackTree()
    values = [3,7,10,12,14,15,16,17,19,20,21,23,26,28,30,41,38,35,39,47]
    for v in values:
        tree.rbinsert(v)
    tree.drawtree()
