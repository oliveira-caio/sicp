tolerance = 1e-5

def is_good_enough(x, y):
    if abs(x-y) < tolerance:
        return True
    return False

def fixed_point(f, x):
    def iterate(f, x, next_value):
        if is_good_enough(x, next_value):
            return next_value
        return iterate(f, next_value, f(next_value))

    return iterate(f, x, f(x))

def f(x):
    return 1 + 1 / x

def main():
    print(fixed_point(f, 1.0))
    
main()
