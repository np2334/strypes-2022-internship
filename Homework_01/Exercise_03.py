def to_number(digits):
    number = 0
    for digit in digits:
        number += digit
        number *= 10

    # заради последната итерация остава в повече едно умножение и го премахвам тук
    number //= 10
    return number

print(to_number([6, 2, 3, 4]))