def for_each(proc, items):
    for item in items:
        proc(item)
    return

def main():
    for_each(lambda x : print(f"{x}"), [57, 321, 88])

main()
