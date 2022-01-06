def accumulate_rec(a, b, neutral, combiner, term, update):
    if a > b:
        return neutral
    return combiner(term(a), accumulate_rec(update(a), b, neutral,
                                            combiner, term, update))

def accumulate_iter(a, b, combiner, term, update, result):
    if a > b:
        return result
    return accumulate_iter(update(a), b, combiner, term,
                           update, combiner(term(a), result))

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

def generalized_prod_rec(a, b, term, update):
    return accumulate_rec(a, b, 1, mul, term, update) 

def generalized_prod_iter(a, b, term, update, result):
    return accumulate_iter(a, b, mul, term, update, 1)

def generalized_sum_rec(a, b, term, update):
    return accumulate_rec(a, b, 0, add, term, update)

def generalized_sum_iter(a, b, term, update, result):
    return accumulate_iter(a, b, add, term, update, 0)

def identity(n):
    return n

def inc(n):
    return n + 1

def cube(n):
    return n ** 3

def factorial_iter(n):    
    return generalized_prod_iter(1, n, identity, inc, 1)

def factorial_rec(n):
    return generalized_prod_rec(1, n, identity, inc)

def term_pi(n):
    if n % 2 == 0:
        return (n + 2) / (n + 1)
    return (n + 1) / (n + 2)

def pi_approx():
    return 4 * generalized_prod_rec(1, 500, term_pi, inc)

def main():
    print(generalized_sum_iter(1, 10, cube, inc, 0))
    print(generalized_sum_rec(1, 10, cube, inc))
    print(generalized_sum_iter(1, 10, identity, inc, 0))
    print(generalized_sum_rec(1, 10, identity, inc))
    print(factorial_iter(4))
    print(factorial_rec(4))
    print(pi_approx())

main()
