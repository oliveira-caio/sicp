class Node():
    def __init__(self, value):
        self.data = value
        self.nextval = None


class Stack():
    def __init__(self, value):
        self.head = Node(value)

    def push_stack(self, value):
        aux = Node(value)
        aux.nextval = self.head
        self.head = aux
        return

    def pop_stack(self):
        aux = self.head
        self.head = self.head.nextval
        return aux

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def print_stack(self):
        while not self.is_empty():
            print(self.head.data)
            self.pop_stack()
        return

class SLinkedList():
    def __init__(self, value):
        self.head = Node(value)

    def add_list(self, value):
        aux = Node(value)
        aux.nextval = self.head
        self.head = aux
        return

    def print_list(self):
        aux = self.head
        while aux is not None:
            print(aux.data)
            aux = aux.nextval
        return

    def reverse(self):
        reversed_list = SLinkedList(self.head.data)
        aux = self.head.nextval
        while aux is not None:
            reversed_list.add_list(aux.data)
            aux = aux.nextval
        return reversed_list

def main():
    one_four = SLinkedList(4)
    one_four.add_list(3)
    one_four.add_list(2)
    one_four.add_list(1)
    one_four.print_list()
    four_one = one_four.reverse()
    four_one.print_list()

main()
