def continued_fraction(N, D, k):
    def iterate(k, current):
        if k == 1:
            return N(1) / current
        return iterate(k-1, D(k-1) + N(k) / current)
    return iterate(k, D(k))

def D(n):
    if n < 1:
        return 1
    if (n+1) % 3 == 0:
        return 2 * D(n-3)
    return 1

def approx_euler_number():
    return 2 + continued_fraction(lambda x : 1,
                                  D,
                                  100)

def main():
    print(approx_euler_number())

main()
