def composition(f):
    def compose(x):
        return f(f(x))
    return compose

def inc(x):
    return x + 1

def main():
    print(composition(inc)(4))
    print(composition(composition(composition))(inc)(5))

main()
