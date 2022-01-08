def cube(n):
    return n ** 3

def simpson_rule(f, a, b, n):
    h = (b - a) / n
    integral_of_f = 0
    values_of_f = [f(a + k*h) for k in range(n + 1)]
    for i, y in enumerate(values_of_f):
        if i == 0 or i == n:
            integral_of_f += y
        elif i % 2 == 1:
            integral_of_f += 4 * y
        else:
            integral_of_f += 2 * y
    return h * integral_of_f / 3

def main():
    print(simpson_rule(cube, 0, 1, 100))
    print(simpson_rule(cube, 0, 1, 1000))

if __name__ == '__main__':
    main()
