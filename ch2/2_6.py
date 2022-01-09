def zero(f):
    return lambda x : x

def one(f):
    return lambda x : f(x)

def two(f):
    return lambda x : f(f(x))

def add_one(n):
    def comp(f):
        def applicate(x):
            return f(n(f)(x))
        return applicate
    return comp

def addition(m, n):
    def comp(f):
        def applicate(x):
            return m(f)(n(f)(x))
        return applicate
    return comp

def square(n):
    return n ** 2

def main():
    print(add_one(two)(square)(5))
    print(addition(two, one)(square)(5))
    
main()
