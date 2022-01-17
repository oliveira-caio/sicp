class Node():
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Tree():
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        self._insert(val, self.root)
        return

    def _insert(self, val, node):
        if val < node.data:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(val, node.left)
        elif val > node.data:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(val, node.right)
        else:
            print("value already inserted.")
        return

    def print_tree(self):
        self._print(self.root)
        return

    def _print(self, node):
        if node is None:
            return
        self._print(node.left)
        print(node.data)
        self._print(node.right)
        return

    def leaves(self):
        return self._leaves(self.root, [])
        
    def _leaves(self, node, items):
        if node.left is None and node.right is None:
            items.append(node.data)
            return items
        if node.left is not None:
            self._leaves(node.left, items)
        if node.right is not None:
            self._leaves(node.right, items)
        return items

def main():
    t = Tree(4)
    t.insert(2)
    t.insert(1)
    t.insert(3)
    t.insert(6)
    t.insert(5)
    t.insert(7)
    t.print_tree()
    print(t.leaves())

main()
