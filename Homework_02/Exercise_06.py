def get_number_length(n):
    length = 0
    while n != 0:
        length += 1
        n //= 10
    return length

def contains_digit(number, digits):
    numberLength = get_number_length(number)

    foundDigitsCount = 0
    for i in range(0, numberLength):
        currentNumber = number % 10
        number //= 10
        
        for j in range(0, len(digits)):
            if digits[j] == currentNumber:
                foundDigitsCount += 1
        
    if foundDigitsCount == len(digits):
        return True
    return False

print(contains_digit(402123, [0, 3, 4]))
print(contains_digit(666, [6, 4]))
print(contains_digit(123456789, [1, 2, 3, 0]))
print(contains_digit(456, []))
print(contains_digit(789456, [7, 6]))
print(contains_digit(2222262222, [8, 6, 1]))
print(contains_digit(2222222222, [1, 3, 4, 5, 6, 7]))


