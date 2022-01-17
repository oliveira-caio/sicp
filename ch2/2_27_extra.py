class Node():
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Tree():
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        self._insert(self.root, val)
        return

    def _insert(self, node, val):
        if val < node.data:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(node.left, val)
        elif val > node.data:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(node.right, val)
        else:
            print("value already inserted.")
        return

    def print_tree(self):
        self._print_tree(self.root)
        return

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(node.data)
            self._print_tree(node.right)
        return

    def deep_reverse(self):
        self._dp(self.root)
        return

    def _dp(self, node):
        if node is None:
            return
        if node.left is not None or node.right is not None:
            aux = node.left
            node.left = node.right
            node.right = aux
            self._dp(node.left)
            self._dp(node.right)
        return

def main():
    t = Tree(7)
    t.insert(2)
    t.insert(4)
    t.insert(1)
    t.insert(10)
    t.insert(8)
    t.print_tree()
    t.deep_reverse()
    t.print_tree()

main()
