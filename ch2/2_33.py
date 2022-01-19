def accumulate(operation, initial, sequence):
    if len(sequence) == 0:
        return initial
    return operation(sequence[0], accumulate(operation, initial, sequence[1:]))

def map_with_accumulate(f, sequence):
    return accumulate(lambda x, y : [f(x)] + y, [], sequence)

def append_with_accumulate(first, second):
    return accumulate(lambda x, y : x + y, [], [first, second])

def length_with_accumulate(sequence):
    return accumulate(lambda x, y : 1 + y, 0, sequence)

def square(x):
    return x * x

def main():
    print(map_with_accumulate(square, [1, 2, 3]))
    print(append_with_accumulate([1], [2]))
    print(length_with_accumulate([]))

main()
