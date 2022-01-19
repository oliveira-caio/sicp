class Branch():
    def __init__(self, length, struct):
        self.length = length
        self.struct = struct # a weight or a binary mobile

    def branch_struct(self):
        return self.struct

    def branch_length(self):
        return self.length

    def torque(self):
        struct = self.branch_struct()
        length = self.branch_length()
        if isinstance(struct, int):
            return struct * length
        return struct.total_weight() * length

class BinaryMobile():
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def left_branch(self):
        return self.left

    def right_branch(self):
        return self.right

    def total_weight(self):
        l = self.left.branch_struct()
        r = self.right.branch_struct()
        if isinstance(l, int) and isinstance(r, int):
            return l + r
        elif isinstance(l, int):
            return l + r.total_weight()
        elif isinstance(r, int):
            return l.total_weight() + r
        else:
            return l.total_weight() + r.total_weight()

    def is_balanced(self):
        if self.left.torque() != self.right.torque():
            return False
        l = self.left.branch_struct()
        r = self.right.branch_struct()
        if all([isinstance(l, int), isinstance(r, int)]):
            return True # essentially because the torque was already computed
        elif isinstance(l, int):
            return r.is_balanced()
        elif isinstance(r, int):
            return l.is_balanced()
        else:
            return l.is_balanced() and r.is_balanced()

def main():
    b_lll = Branch(1, 13)
    b_llr = Branch(2, 13)
    b_ll = BinaryMobile(b_lll, b_llr)
    b_l = Branch(1, b_ll)
    b_rrl = Branch(1, 13)
    b_rrr = Branch(1, 13)
    b_rr = BinaryMobile(b_rrl, b_rrr)
    b_r = Branch(1, b_rr)
    bm = BinaryMobile(b_l, b_r)
    print(bm.total_weight())
    print(bm.is_balanced())
    bp_l = Branch(1, 4)
    bp_rrl = Branch(1, 2)
    bp_rrr = Branch(1, 2)
    bp_rr = BinaryMobile(bp_rrl, bp_rrr)
    bp_r = Branch(1, bp_rr)
    bpm = BinaryMobile(bp_l, bp_r)
    print(bpm.total_weight())
    print(bpm.is_balanced())

main()
