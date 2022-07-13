def func(some_list, num):
    temp = []
    for i in range(0, len(some_list)):
        firstNumber = some_list[i]

        for j in range(i + 1, len(some_list)):

            secondNumber = some_list[j]
            if firstNumber + secondNumber == num:
                temp.append([firstNumber, secondNumber])

    return tuple(temp)

print(func([9, 8, 7, 6, 5, 4, 3, 2, 1], 8))
print(func([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
print(func([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
print(func([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
print(func([1, 2, 3, 4, 5, 6, 7, 8, 9], 22))