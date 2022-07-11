import sys

def find_min_number(arr):
    # исках да използвам еквивалента на Int32.MaxValue в C# за да мога да сравня всяка стойност от масива с тази и да намеря най-малката възможна
    smallestNumber = sys.maxsize

    for i in range(0, len(arr)):
        currentNumber = arr[i]
        if currentNumber < smallestNumber:
            smallestNumber = currentNumber

    return smallestNumber

def find_max_number(arr):
    # пробвах да добавя 1 и да пробвам да накарам променливата да overflow-не и да започне от най-ниската стойност, но по някаква причина това не се получава, защо?
    # защо мога да добавя след това примерно 59941 към maxsize и не overflow-ва? какво определя размера на типа? 
    biggestNumber = -sys.maxsize

    for i in range(0, len(arr)):
        currentNumber = arr[i]
        if currentNumber > biggestNumber:
            biggestNumber = currentNumber
    
    return biggestNumber

def sum_of_min_and_max(arr):
    return find_min_number(arr) + find_max_number(arr)

print(sum_of_min_and_max([1, 2, 3, 4, 5, 6, 8, 9]))
print(sum_of_min_and_max([-10, 5, 10, 100]))
print(sum_of_min_and_max([1]))
print(sum_of_min_and_max([]))
print(sum_of_min_and_max([1, 2, 3, -100, 5, 6, 2, 10, 10, 205, 55]))