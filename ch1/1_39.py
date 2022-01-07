def continued_fraction(N, D, k):
    def iterate(k, current):
        if k == 1:
            return N(1) / current
        return iterate(k-1, D(k-1) - N(k) / current)
    return iterate(k, D(k))

def N(x):
    def seq(n):
        if n == 1:
            return x
        return x ** 2
    return seq

def D(n):
    return 2*n - 1

def tan_cf(x):
    return continued_fraction(N(x), D, 100)

def main():
    print(tan_cf(1))

main()
