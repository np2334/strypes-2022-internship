my_set = (2, 4, 10, 3)
new_list = [element * element for element in my_set]

print(new_list)

new_dictionary = {element:element * element for i, element in enumerate(my_set) if element % 2 == 0 and i % 2 != 0}
print(new_dictionary)