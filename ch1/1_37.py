import math


tolerance = 1e-5

def is_good_enough(x, y):
    if abs(x - y) < tolerance:
        return True
    return False

def continued_fraction_rec(N, D, k, counter=1):
    if counter == k:
        return N(k) / D(k)
    return N(counter) / (D(counter) + continued_fraction_rec(N, D, k, counter+1))

def continued_fraction_iter(N, D, k):
    def iterate(k, current):
        if k == 1:
            return N(1) / current
        return iterate(k-1, D(k-1) + N(k) / current)
    return iterate(k, D(k))

def main():
    i, j = 1, 1
    golden_ratio = (1 + math.sqrt(5)) / 2
    while not is_good_enough(golden_ratio,
                             1 / continued_fraction_rec(lambda x : 1,
                                                        lambda x : 1,
                                                        i)):
        i += 1
    while not is_good_enough(golden_ratio,
                             1 / continued_fraction_iter(lambda x : 1,
                                                         lambda x : 1,
                                                         j)):
        j += 1
    print(i, j)

main()
