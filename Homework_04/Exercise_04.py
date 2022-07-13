def func(some_list, num):
    temp = []
    for i in range(0, len(some_list)):
        firstNumber = some_list[i]

        for j in range(0, len(some_list)):
            # да не се повтарят
            if i == j or pair_is_contained(temp, ):
                continue

            secondNumber = some_list[j]
            if firstNumber + secondNumber == num:
                temp.append([firstNumber, secondNumber])

    return tuple(temp)

print(func([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
print(func([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
print(func([1, 2, 3, 4, 5, 6, 7, 8, 9], 22))