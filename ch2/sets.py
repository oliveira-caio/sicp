class SetUnorderedList():
    
    def __init__(self, elems=[]):
        self.elems = elems

    def __str__(self):
        return f"{self.elems}"

    def is_element(self, x):
        for elem in self.elems:
            if elem == x:
                return True
        return False

    def adjoin(self, x):
        self.elems.append(x)

    @staticmethod
    def intersection(set_one, set_two):
        if len(set_one.elems) == 0:
            return SetUnorderedList()
        elif set_two.is_element(set_one.elems[0]):
            inter = SetUnorderedList.intersection(
                SetUnorderedList(set_one.elems[1:]),
                set_two
            )
            inter.adjoin(set_one.elems[0])
            return inter
        else:
            return SetUnorderedList.intersection(
                SetUnorderedList(set_one.elems[1:]),
                set_two
            )

    @staticmethod
    def union(set_one, set_two):
        if len(set_one.elems) == 0:
            return SetUnorderedList(set_two.elems)
        elif set_two.is_element(set_one.elems[0]):
            return SetUnorderedList.union(
                SetUnorderedList(set_one.elems[1:]),
                set_two
            )
        else:
            un = SetUnorderedList.union(
                SetUnorderedList(set_one.elems[1:]),
                set_two
            )
            un.adjoin(set_one.elems[0])
            return un

class SetOrderedList():

    def __init__(self, elems=[]):
        self.elems = elems

    def __str__(self):
        return f"{self.elems}"

    @staticmethod
    def binary_search(sequence, x, boolean=True):
        n = len(sequence)
        if n == 0:
            if boolean:
                return True
            return 0
        l, mid, r = 0, n // 2, n
        while l <= r:
            if sequence[mid] == x:
                if boolean:
                    return True
                return mid
            elif sequence[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
            mid = l + (r - l) // 2
        if boolean:
            return False
        return mid

    def is_element(self, x):
        return SetOrderedList.binary_search(self.elems, x, True)

    def adjoin(self, x):
        index = SetOrderedList.binary_search(self.elems, x, False)
        self.elems.insert(index, x)

    @staticmethod
    def intersection(set_one, set_two):
        if len(set_one.elems) == 0 or len(set_two.elems) == 0:
            return SetOrderedList()
        elif set_one.elems[0] == set_two.elems[0]:
            aux = SetOrderedList([set_one.elems[0]])
            inter = SetOrderedList.intersection(
                SetOrderedList(set_one.elems[1:]),
                SetOrderedList(set_two.elems[1:]),
            )
            aux.elems.extend(inter.elems)
            return aux
        elif set_one.elems[0] < set_two.elems[0]:
            return SetOrderedList.intersection(
                SetOrderedList(set_one.elems[1:]),
                set_two
            )
        else:
            return SetOrderedList.intersection(
                    set_one,
                    SetOrderedList(set_two.elems[1:])
                )

    @staticmethod
    def union(set_one, set_two):
        un = SetOrderedList()
        aux = SetOrderedList()
        if len(set_one.elems) == 0:
            return set_two
        elif len(set_two.elems) == 0:
            return set_one
        elif set_one.elems[0] == set_two.elems[0]:
            un.elems = set_one.elems[:1]
            aux = SetOrderedList.union(
                SetOrderedList(set_one.elems[1:]),
                SetOrderedList(set_two.elems[1:])
            )
        elif set_one.elems[0] < set_two.elems[0]:
            un.elems = set_one.elems[:1]
            aux = SetOrderedList.union(
                SetOrderedList(set_one.elems[1:]),
                set_two
            )
        else:
            un.elems = set_two.elems[:1]
            aux = SetOrderedList.union(
                set_one,
                SetOrderedList(set_one.elems[1:]),
            )
        un.elems.extend(aux.elems)
        return un

def main():
    s1 = SetUnorderedList([1, 2, 3])
    s2 = SetUnorderedList([2, 3])
    print(s1)
    print(s1.is_element(2))
    print(s1.is_element(4))
    print(SetUnorderedList.intersection(s1, s2))
    print(SetUnorderedList.union(s1, s2))
    s3 = SetOrderedList([4, 5, 6])
    s4 = SetOrderedList([4, 6, 8])
    print(s3)
    print(s3.is_element(2))
    print(s3.is_element(4))
    print(SetOrderedList.intersection(s3, s4)) 
    print(SetOrderedList.union(s3, s4))

main()
