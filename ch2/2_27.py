def reverse(items):
    stack = []
    for item in items:
        stack.append(item)
    for i in range(len(items)):
        items[i] = stack.pop()
    return

def deep_reverse(items):
    if not isinstance(items, list) or len(items) == 1:
        return items
    for item in items:
        deep_reverse(item)
    reverse(items)
    return items

def main():
    tree = [[[1, 2], 3], [4, [[5], [6]]]]
    print(deep_reverse(tree))

main()
