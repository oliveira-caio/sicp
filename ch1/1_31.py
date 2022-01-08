def generalized_prod_rec(a, b, term, update):
    if a > b:
        return 1
    return term(a) * generalized_prod_rec(update(a), b, term, update)

def generalized_prod_iter(a, b, term, update, result):
    if a > b:
        return result
    return generalized_prod_iter(update(a), b, term, update, result * term(a))

def identity(n):
    return n

def inc(n):
    return n + 1

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
    print(factorial_iter(4))
    print(factorial_rec(4))
    print(pi_approx())

if __name__ == '__main__':
    main()
