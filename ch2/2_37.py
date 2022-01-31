def accumulate(op, init, seq):
    if len(seq) == 0:
        return init
    return op(seq[0], accumulate(op, init, seq[1:]))

def accumulate_n(op, init, seqs):
    if len(seqs[0]) == 0:
        return []
    return ([accumulate(op, init, [seq[0] for seq in seqs])]
            + accumulate_n(op, init, [seq[1:] for seq in seqs]))

def my_map(f, seqs):
    if len(seqs[0]) == 0:
        return []
    return ([f([seq[0] for seq in seqs])]
            + my_map(f, [seq[1:] for seq in seqs]))

def prod(seq):
    if len(seq) == 0:
        return 1
    res = 1
    for s in seq:
        res *= s
    return res

def dot_prod(v, w):
    return accumulate(lambda x, y : x + y, 0, my_map(prod, [v, w]))

def matrix_vector(m, v):
    return my_map(lambda x : dot_prod(x, v), m)

def main():
    m = [[1, 2, 3, 4], [4, 5, 6, 6], [6, 7, 8, 9]]
    v = [1, 2, 3, 4]
    w = [4, 5, 6, 6]
    # print(my_map(sum, [[1, 2, 3, 4], [40, 50, 60, 70], [700, 800, 900, 1000]]))
    print(dot_prod(v, w))
    print(matrix_vector(m, v))

main()
