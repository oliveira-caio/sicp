def accumulate(op, init, seq):
    if len(seq) == 0:
        return init
    return op(seq[0], accumulate(op, init, seq[1:]))

def my_map(f, seq):
    return accumulate(lambda x, y : [f(x)] + y, [], seq)

def ordered_triples(n):
    return my_map(
        lambda i : my_map(
            lambda j : my_map(
                lambda k : [i, j, k], range(1, j)
            ),
            range(2, i)
        ),
        range(3, n+1)
    )

def flatmap(proc, seq):
    return accumulate(lambda x, y : x+y, [], my_map(proc, seq))

def is_sum(s):
    def check(triple):
        if triple[0] + triple[1] + triple[2] == s:
            return True
        return False
    return check

def my_filter(predicate, seq):
    return [s for s in seq if predicate(s)]

def triples_sum_s(s, n):
    return my_filter(is_sum(s),
                     flatmap(identity,
                             flatmap(identity,
                                     ordered_triples(n))))


def identity(x):
    return x

def main():
    print(triples_sum_s(23, 20))

main()
