def int_abs(n):
    if n < 0:
        n *= -1
    return n

def sum_of_digits(n):
    sum = 0
    n = int_abs(n)
    # така работи само за трицифрени цели числа
    for i in range(0, 4):
        sum += n % 10
        n //= 10
    return sum

print(sum_of_digits(-123))
