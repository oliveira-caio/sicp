def composition(f, g):
    def application(x):
        return f(g(x))
    return application

def repeated(f, n):
    if n == 1:
        return f
    return composition(f, repeated(f, n-1))

def main():
    print(repeated(lambda x : x**2, 2)(5))

main()
