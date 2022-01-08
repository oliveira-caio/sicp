def filtered_accumulate(a, b, term, update, combiner, neutral, predicate):
    if a > b:
        return neutral
    if predicate(a):
        return combiner(term(a), filtered_accumulate(update(a),
                                                     b,
                                                     term,
                                                     update,
                                                     combiner,
                                                     neutral,
                                                     predicate))
    return filtered_accumulate(update(a), b, term, update,
                               combiner, neutral, predicate)

def smallest_divisor(n, test=2):
    if test ** 2 > n:
        return n
    if n % test == 0:
        return test
    if test == 2:
        return smallest_divisor(n, test+1)
    return smallest_divisor(n, test+2)

def is_prime(n):
    if smallest_divisor(n) == n:
        return True
    return False

def inc(n):
    return n + 1

def square(n):
    return n ** 2

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def gcd(a, b):
    if b == 0:
        return a
    if a > b:
        return gcd(b, a % b)
    return gcd(a, b % a)

def is_relative_prime_to_n(n):
    def is_relative_prime(a):
        if gcd(a, n) == 1:
            return True
        return False
    return is_relative_prime

def identity(n):
    return n

def main():
    print(filtered_accumulate(2, 10, square, inc, add, 0, is_prime))
    print(filtered_accumulate(1, 10, identity, inc, mul, 1,
                              is_relative_prime_to_n(10)))

if __name__ == '__main__':
    main()
