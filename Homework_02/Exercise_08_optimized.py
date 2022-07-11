import sys

# след като направих задачата с итериране върху всеки елемент и итериране върху масива за всеки елемент стигнах до
# заключението, че няма смисъл да правя N * N итерации (примерно ако имаме 5 елемента 5 * 5 = 25 итерации), а мога директно
# да намеря най-малкото число и най-голямото и да ги изкарам, така ще получа възможно най-голямата разлика с 2 * N итерации

def find_min_number(arr):
    smallestNumber = sys.maxsize

    for i in range(0, len(arr)):
        currentNumber = arr[i]
        if currentNumber < smallestNumber:
            smallestNumber = currentNumber

    return smallestNumber

def find_max_number(arr):
    biggestNumber = -sys.maxsize

    for i in range(0, len(arr)):
        currentNumber = arr[i]
        if currentNumber > biggestNumber:
            biggestNumber = currentNumber
    
    return biggestNumber

def biggest_difference(arr):
    return find_min_number(arr) - find_max_number(arr)

print(biggest_difference([1, 2]))
print(biggest_difference([1, 2, 3, 4, 5]))
print(biggest_difference([-10, -9, -1]))
print(biggest_difference(range(100)))