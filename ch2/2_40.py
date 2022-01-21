def accumulate(op, init, seq):
    if len(seq) == 0:
        return init
    return op(seq[0], accumulate(op, init, seq[1:]))

def my_map(f, seq):
    return accumulate(lambda x, y : [f(x)] + y, [], seq)

def flatmap(proc, seq):
    return accumulate(lambda x, y : x+y, [], my_map(proc, seq))

def unique_pair(n):
    return my_map(lambda i : my_map(lambda j : [i, j],
                                    range(1, i)),
                  range(2, n+1))

def smallest_divisor(n):
    def in_iter(k):
        if k * k <= n:
            if n % k == 0:
                return k
            else:
                return in_iter(k+1)
        return n
    return in_iter(2)

def is_prime(n):
    if smallest_divisor(n) == n:
        return True
    return False

def is_sum_prime(pair):
    if is_prime(pair[0] + pair[1]):
        return True
    return False

def make_pair_sum(pair):
    return [pair[0], pair[1], pair[0] + pair[1]]

def my_filter(predicate, seq):
    return [s for s in seq if predicate(s)]

def sum_pairs_prime(n):
    return my_map(make_pair_sum,
                  my_filter(is_sum_prime,
                            flatmap(identity,
                                    unique_pair(n))))

def identity(x):
    return x

def main():
    print(sum_pairs_prime(10))

main()
