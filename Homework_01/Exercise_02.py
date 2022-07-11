def reverse_list(list):
    reversedList = []
    for item in range(len(list) - 1, -1, -1):
        reversedList.append(list[item])
    return reversedList

def to_digits(n):
    list = []
    while n != 0:
        list.append(n % 10)
        n //= 10
    return list

list = to_digits(2568)
print(reverse_list(list))
