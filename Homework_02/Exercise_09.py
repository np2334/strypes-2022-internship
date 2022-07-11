import sys

def round_float_ending(floatNumber):
    # умножавам по 100 за да преместя с 2 позиции първите 2 числа от дясно на точката 
    # 123.634144444 * 100 = 12363.4144444
    floatNumber *= 100
    # cast-вам го на цяло число за да премахна ненужната част след точката
    # (int)12363.4144444 = 12363
    floatNumber = int(floatNumber)
    # разделям го на 100.0 (представено като тип с плаваща запетая зад а върне число с плаваща запетая, за да мога да върна 2те взети числа от дясно на запетаята
    # 12363 / 100.0 = 123.63
    floatNumber /= 100.0

    return floatNumber

def find_biggest_value_index(array):
    biggestValueIndex = -1
    biggestValue = -sys.maxsize

    for i in range(0, len(array)):
        currentValue = array[i]

        if currentValue > biggestValue:
            biggestValue = currentValue
            biggestValueIndex = i
    
    return biggestValueIndex

def find_smallest_value_index(array):
    smallestValueIndex = -1
    smallestValue = sys.maxsize

    for i in range(0, len(array)):
        currentValue = array[i]

        if currentValue < smallestValue:
            smallestValue = currentValue
            smallestValueIndex = i

    return smallestValueIndex


def slope_style_score(scores):
    smallestValueIndex = find_smallest_value_index(scores)
    biggestValueIndex = find_biggest_value_index(scores)

    sum = 0
    for i in range(0, len(scores)):
        if i != smallestValueIndex and i != biggestValueIndex:
            sum += scores[i]

    return sum / (len(scores) - 2)

print(round_float_ending(slope_style_score([94, 95, 95, 95, 90])))
print(round_float_ending(slope_style_score([60, 70, 80, 90, 100])))
print(round_float_ending(slope_style_score([96, 95.5, 93, 89, 92])))
