def func(some_list, num):
    # new_list = [[[example_list[i], example_list[j]] for j in range(i + 1, len(example_list)) if example_list[i] + example_list[j] == sum] for i in range(0, len(example_list))]
    # понеже ползвам list comprehension в list comprehension и в него правя масив от 2 елемента получавам това като резултат
    # [[[1, 7]], [[2, 6]], [[3, 5]], [], [], [], [], [], []]
    # след това правя още един list comprehension за всеки елемент от получения резултат и взимам за всеки елемент първия и втория елемент ако масива има елементи
    # [[1, 7]], [[2, 6]], [[3, 5]] за всеки елемент => [element[0][0], element[0][1]] за да изкарам числата от вътрешния списък

    new_list = [[element[0][0], element[0][1]] for element in [[[some_list[i], some_list[j]] for j in range(i + 1, len(some_list)) if some_list[i] + some_list[j] == num] for i in range(0, len(some_list))] if len(element) > 0]
    return tuple(new_list)

print(func([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
print(func([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
print(func([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
print(func([1, 2, 3, 4, 5, 6, 7, 8, 9], 22))