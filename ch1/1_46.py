tolerance = 1e-5

def iterative_improve(is_good_enough, improve_guess):
    def iterate(guess):
        improved = improve_guess(guess)
        if is_good_enough(guess, improved):
            return improved
        return iterate(improved)
    return iterate

def good_enough(x, y):
    if abs(x-y) < tolerance:
        return True
    return False

def fixed_point(f):
    return iterative_improve(good_enough, f)(1.0)

def my_sqrt(x):
    def improve(y):
        return (y + x/y) / 2
    return iterative_improve(good_enough, improve)(1.0)

def main():
    print(fixed_point(lambda x : 2))
    print(my_sqrt(9))

main()
