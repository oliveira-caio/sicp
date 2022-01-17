class Branch():
    def __init__(self, length, structure):
        self.length = length
        self.structure = structure

class Binary_Mobile():
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def total_weight(self):
        if isinstance(self.left.structure, int) and isinstance(self.right.structure, int):
            return self.left.structure + self.right.structure
        elif isinstance(self.left.structure, int):
            return self.left.structure + self.right.structure.total_weight()
        elif isinstance(self.right.structure, int):
            return self.right.structure + self.left.structure.total_weight()
        else:
            return (self.left.structure.total_weight()
                    + self.right.structure.total_weight())

    def is_balanced(self):
        if isinstance(self.left.structure, int) and isinstance(self.right.structure, int):
            return (self.left.structure * self.left.length == self.right.structure * self.right.length)
        elif isinstance(self.left.structure, int):
            return False
        elif isinstance(self.right.structure, int):
            return False
        else:
            return (self.left.structure.is_balanced() and self.right.structure.is_balanced())

def main():
    b_lll = Branch(1, 13)
    b_llr = Branch(2, 13)
    b_ll = Binary_Mobile(b_lll, b_llr)
    b_l = Branch(1, b_ll)
    b_rrl = Branch(1, 13)
    b_rrr = Branch(1, 13)
    b_rr = Binary_Mobile(b_rrl, b_rrr)
    b_r = Branch(1, b_rr)
    bm = Binary_Mobile(b_l, b_r)
    print(bm.total_weight())
    print(bm.is_balanced())

main()
