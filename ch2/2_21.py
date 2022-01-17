def square_list(items):
    if len(items) == 1:
        return [items[0] ** 2]
    return [items[0] ** 2] + square_list(items[1:])

def my_map(f, items):
    mapped = []
    for item in items:
        mapped.append(f(item))
    return mapped

def map_square_list(items):
    return my_map(lambda x : x ** 2, items)

def main():
    print(square_list([1, 2, 3, 4]))
    print(map_square_list([1, 2, 3, 4]))

main()
