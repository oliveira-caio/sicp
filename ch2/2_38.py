def fold_left(op, init, seq):
    def inner_iter(result, rest):
        if len(rest) == 0:
            return result
        return inner_iter(op(result, rest[0]), rest[1:])
    return inner_iter(init, seq)

def fold_right(op, init, seq):
    def inner_iter(result, rest):
        if len(rest) == 0:
            return result
        return op(rest[0], inner_iter(result, rest[1:]))
    return inner_iter(init, seq)

def main():
    x = [1, 2, 3]
    print(fold_left(lambda x, y : x + y, 0, x))
    print(fold_right(lambda x, y : x + y, 0, x))
    
main()
