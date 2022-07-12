def count_words(arr):
    count_dictionary = {}

    for element in arr:
        # if element in count_dictionary 
        if count_dictionary.get(element) == None:
            count_dictionary[element] = 1
        else:
            count_dictionary[element] += 1
            
    return count_dictionary

print(count_words(["apple", "banana", "apple", "pie"]))
print(count_words(["python", "python", "python", "ruby"]))
