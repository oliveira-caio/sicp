def accumulate(operation, initial, sequence):
    if len(sequence) == 0:
        return initial
    return operation(sequence[0], accumulate(operation, initial, sequence[1:]))

def enumerate_tree(t):
    if isinstance(t, int):
        return [t]
    elif len(t) == 0:
        return []
    else:
        return enumerate_tree(t[0]) + enumerate_tree(t[1:])

def my_map(seq):
    return [1 for s in seq]

def count_leaves(t):
    return accumulate(lambda x, y : x + y, 0, my_map(enumerate_tree(t)))

def main():
    t = [1, [2, [3, 4]], 5]
    print(count_leaves(t))
    print(count_leaves(t + t))
    print(count_leaves(t + t + t))

main()
