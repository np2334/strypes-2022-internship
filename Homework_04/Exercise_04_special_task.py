def func(some_list, num):
    # TODO
    new_list = [[x, y] for x, y in some_list]

    return tuple(new_list)

print(func([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
print(func([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
print(func([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
print(func([1, 2, 3, 4, 5, 6, 7, 8, 9], 22))