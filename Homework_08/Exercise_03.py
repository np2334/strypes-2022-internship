list_of_numbers = [1, 1, 1, 2, 3, 3, 4, 5, 5, 5, 5, 5, 5]


dictionary_of_numbers = {}
for number in list_of_numbers:
    try:
        dictionary_of_numbers[number] += 1
    except KeyError:
        dictionary_of_numbers[number] = 1

print(dictionary_of_numbers)