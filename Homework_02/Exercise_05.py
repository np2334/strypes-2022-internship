def get_number_length(n):
    length = 0
    while n != 0:
        length += 1
        n //= 10
    return length

def contains_digit(number, digit):
    numberLength = get_number_length(number)
    
    for i in range(0, numberLength):
        currentNumber = number % 10
        number //= 10
        if currentNumber == digit:
            return True
    return False

print(contains_digit(123, 4))
print(contains_digit(42, 2))
print(contains_digit(1000, 0))
print(contains_digit(12346789, 5))
print(contains_digit(789456, 7))
print(contains_digit(2222222222, 7))

