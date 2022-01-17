def sublists(plist):
    if len(plist) == 0:
        return [[]]
    x = plist[0]
    subl = sublists(plist[1:])
    return subl + [[x] + s for s in subl]

def main():
    a = [1, 2, 3, 4]
    print(sublists(a))

main()
