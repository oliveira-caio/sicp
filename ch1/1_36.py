from math import log


tolerance = 1e-5

def is_good_enough(x, y):
    if abs(x-y) < tolerance:
        return True
    return False

def fixed_point(f, x):
    def iterate(f, x, next_value, n_iter):
        if is_good_enough(x, next_value):
            return next_value, n_iter
        n_iter += 1
        return iterate(f, next_value, f(next_value), n_iter)
    return iterate(f, x, f(x), 0)

def x_to_the_x(x):
    return log(1000) / log(x)

def x_to_the_x_damped(x):
    return (x + log(1000) / log(x)) / 2

def main():
    print(fixed_point(x_to_the_x, 2.0))
    print(fixed_point(x_to_the_x_damped, 2.0))

main()
