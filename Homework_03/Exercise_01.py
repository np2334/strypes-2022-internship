import sys

def sum_dictionary_values(dictionary, odd_numbers = True):
        sum = 0
        for keys in dictionary.keys():
            current_value = dictionary.get(key)

            if odd_numbers:
                if current_value % 2 != 0:
                    sum += current_value
            else:
                if current_value % 2 == 0:
                    sum += current_value               
        return sum


dictionary_of_people = {
    "Pesho": 10,
    "Gosho": 40,
    "Stanko": 20
}

dictionary_of_people["Kiril"] = 41

for key, value in dictionary_of_people.items():
    print(value)

for value in dictionary_of_people.values():
    print(value)


print(sum_dictionary_values(dictionary_of_people))
print(sum_dictionary_values(dictionary_of_people, False))