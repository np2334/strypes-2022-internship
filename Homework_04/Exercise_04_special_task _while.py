def func(some_list, num):
    first_index = some_list[0]
    last_index = some_list[len(some_list) - 1]
    new_list = []

    while(first_index == last_index):
        first_element = some_list[first_index]
        second_element = some_list[last_index]
        

    return tuple(new_list)

print(func([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))