import sys

def group(array):
    list_of_groups = []
    list_of_inner_groups = []
    last_number = array[0]

    list_of_inner_groups.append(last_number)
    
    for i in range(1, len(array)):
        current_number = array[i]
        
        if current_number == last_number:
            list_of_inner_groups.append(current_number)
        else:
            list_of_groups.append(list_of_inner_groups)
            list_of_inner_groups = []
            list_of_inner_groups.append(current_number)

        last_number = current_number

    if len(list_of_inner_groups) != 0:
        list_of_groups.append(list_of_inner_groups)
    return list_of_groups


def max_consecutive(array):
    biggest_group_count = -sys.maxsize

    list_of_groups = group(array)
    for current_group in list_of_groups:
        if biggest_group_count < len(current_group):
            biggest_group_count = len(current_group)
    return biggest_group_count
        


#print(group([1, 1, 1, 2, 3, 1, 1]))
#print(group([1, 2, 1, 2, 3, 3]))
print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
