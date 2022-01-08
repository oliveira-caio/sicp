tolerance = 1e-5
dx = 1e-5

def cubic(a, b, c):
    def f(x):
        return x**3 + a * x**2 + b * x + c
    return f

def is_good_enough(x, y):
    if abs(x - y) < tolerance:
        return True
    return False

def fixed_point(f, guess):
    if is_good_enough(guess, f(guess)):
        return f(guess)
    return fixed_point(f, f(guess))

def derivative(f):
    def f_prime(x):
        return (f(x+dx) - f(x-dx)) / (2 * dx)
    return f_prime

def newton_transform(f):
    def transformed(x):
        return x - f(x) / derivative(f)(x)
    return transformed

def newton_method(f, guess):
    return fixed_point(newton_transform(f), guess)

def main():
    print(newton_method(cubic(0, 0, -8), 1.0))

main()
          
