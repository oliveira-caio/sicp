def same_parity(one, *args):
    parity = one % 2
    pars = [one]
    for x in args:
        if x % 2 == parity:
            pars.append(x)
    return pars

def main():
    print(same_parity(1, 2, 3, 4, 5, 6, 7))
    print(same_parity(2, 3, 4, 5, 6, 7))

main()
