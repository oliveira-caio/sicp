dx = 1e-5

def smooth(f):
    return (lambda x : (f(x+dx) + f(x) + f(x-dx)) / 3)

def compose(f, g):
    return (lambda x : f(g(x)))

def repeated(f, n):
    if n == 1:
        return f
    return compose(f, repeated(f, n-1))

def n_fold_smooth(f, n):
    return smooth(repeated(f, n))

def main():
    print(n_fold_smooth(lambda x : x, 3)(2))

main()


