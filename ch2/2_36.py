def accumulate(operation, initial, seq):
    if len(seq) == 0:
        return initial
    return operation(seq[0], accumulate(operation, initial, seq[1:]))

def accumulate_n(operation, initial, seqs):
    if len(seqs[0]) == 0:
        return []
    return ([accumulate(operation, initial, [seq[0] for seq in seqs])]
            + accumulate_n(operation, initial, [seq[1:] for seq in seqs]))

def main():
    s = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    print(accumulate_n(lambda x, y : x + y, 0, s))

main()
