def equal(l1, l2):
    if len(l1) != len(l2):
        return False
    if len(l1) == 0:
        return True
    return l1[0] == l2[0] and equal(l1[1:], l2[1:])

def main():
    print(equal(['a'], ['a']))
    print(equal([1, 2], [3]))
    print(equal(['this', 'is', 'a', 'list'],
                ['this', '(is)', 'a', 'list']))

main()
