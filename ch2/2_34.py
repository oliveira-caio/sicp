def accumulate(operation, initial, sequence):
    if len(sequence) == 0:
        return initial
    return operation(sequence[0], accumulate(operation, initial, sequence[1:]))

def horner_eval(x, coeffs):
    return accumulate(lambda cur, higher : cur + x * higher, 0, coeffs)

def main():
    print(horner_eval(2, [1, 3, 0, 5, 0, 1]))

main()
