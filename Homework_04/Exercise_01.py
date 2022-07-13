def second_function(tupl):
    temp_list = []
    for element in tupl:
        if isinstance(element, str):
            temp_list.append(1)
        else:
            temp_list.append(element)
    return (temp_list)

def first_function(tupl):
    for element in tupl:
        #if type(element) == type(list):
        if isinstance(element, list):
            for i in range(0, len(element)):
                element[i] = 0
    
arr = (1, 2, [22, 44], "a", 5, [0, 0], 1)
first_function(arr)

print(second_function(arr))


