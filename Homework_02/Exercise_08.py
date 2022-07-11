import sys

def biggest_difference(arr):
    # тук отново искам да използвам еквивалента на Int32.MaxValue
    biggestDifference = sys.maxsize

    for i in range(0, len(arr)):
        firstNumber = arr[i]

        for j in range(0, len(arr)):
            if i == j:
                continue
            secondNumber = arr[j] 

            biggestNumberDifference = firstNumber - secondNumber
            if secondNumber - firstNumber < biggestDifference:
                biggestDifference = secondNumber - firstNumber

            if biggestNumberDifference < biggestDifference:
                biggestDifference = biggestNumberDifference
    
    return biggestDifference


print(biggest_difference([1, 2]))
print(biggest_difference([1, 2, 3, 4, 5]))
print(biggest_difference([-10, -9, -1]))
print(biggest_difference(range(100)))