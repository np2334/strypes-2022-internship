def add_set_range(my_set):
    list_to_add = [4, 5, 66]
    set_to_add = set({0, 88, 93})

    #for element in lst:
    #    my_set.add(element)
    #for element in spec_set:
    #    my_set.add(element)

    my_set.update(list_to_add)
    my_set.update(set_to_add)

example_set = set()
for i in range(0, 50):
    example_set.add(i)

add_set_range(example_set)
print(example_set)

