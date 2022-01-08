def generalized_sum_rec(a, b, term, update):
    if a > b:
        return 0
    return term(a) + generalized_sum_rec(update(a), b, term, update)

def generalized_sum_iter(a, b, term, update, result):
    if a > b:
        return result
    return generalized_sum_iter(update(a), b, term, update, result + term(a))

def identity(n):
    return n

def inc(n):
    return n + 1

def cube(n):
    return n ** 3

def main():
    print(generalized_sum_iter(1, 10, cube, inc, 0))
    print(generalized_sum_rec(1, 10, cube, inc))

if __name__ == '__main__':
    main()
