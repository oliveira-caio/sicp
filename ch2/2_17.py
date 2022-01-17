class Node():
    def __init__(self, value):
        self.data = value
        self.nextval = None

class SLinkedList():
    def __init__(self, value):
        self.head = Node(value)

    def add_list(self, value):
        aux = Node(value)
        aux.nextval = self.head
        self.head = aux
        return

    def last_element(self):
        if self.head is None:
            return
        aux = self.head
        while aux.nextval is not None:
            aux = aux.nextval
        return SLinkedList(aux.data)

    def print_list(self):
        aux = self.head
        while aux is not None:
            print(aux.data)
            aux = aux.nextval
        return

def main():
    one_four = SLinkedList(4)
    one_four.add_list(3)
    one_four.add_list(2)
    one_four.add_list(1)
    four = one_four.last_element()
    four.add_list(10)
    four.print_list()

main()
