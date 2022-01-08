def compose(f, g):
    def f_circ_g(x):
        return f(g(x))
    return f_circ_g

def main():
    print(compose(lambda x : x**2, lambda x : x+1)(6))

main()
