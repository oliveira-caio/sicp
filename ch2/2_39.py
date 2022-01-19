def fold_left(op, init, seq):
    def inner_iter(result, rest):
        if len(rest) == 0:
            return result
        return inner_iter(op(rest[0], result), rest[1:])
    return inner_iter(init, seq)

def fold_right(op, init, seq):
    def inner_iter(result, rest):
        if len(rest) == 0:
            return result
        return op(rest[0], inner_iter(result, rest[1:]))
    return inner_iter(init, seq)

def reverse_left(seq):
    return fold_left(lambda x, y : [x] + y, [], seq)

def reverse_right(seq):
    return fold_right(lambda x, y : y + [x], [], seq)

def main():
    x = [1, 2, 3, 4]
    print(reverse_left(x))
    print(reverse_right(x))

main()
