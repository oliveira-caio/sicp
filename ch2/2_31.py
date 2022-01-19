def square(x):
    return x ** 2

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        print(self.data)
        if self.right is not None:
            self.right.print_tree()
        return

    def insert_tree(self, val):
        if val < self.data:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert_tree(val)
        else:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert_tree(val)

    def map_tree(self, f):
        if self.left is not None:
            self.left.map_tree(f)
        self.data = f(self.data)
        if self.right is not None:
            self.right.map_tree(f)
        return

    def square_tree(self):
        self.map_tree(square)
        return

def main():
    root = Node(5)
    root.insert_tree(2)
    root.insert_tree(6)
    root.print_tree()
    root.square_tree()
    root.print_tree()

main()
