def get_number_length(n):
    length = 0
    while n != 0:
        n //= 10
        length += 1
    return length

def int_abs(n):
    if n < 0:
        n *= -1
    return n

def fib_number(n):
    n = int_abs(n)

    if n == 0:
        return 0

    sum = 1
    firstNum = 0
    secondNum = 1
    if n > 1:
        for i in range(0, n - 1):
            fib = firstNum + secondNum
            # при 7 числото на фибоначи става с 2 цифри, при 12 числото на фибоначи става с 3 цифри, 
            # т.е. трябва да умножа сумата N на брой пъти според броя на цифрите в числото на фибоначи за да мога да го прибавя и долепя към сумата
            for j in range(0, get_number_length(fib)):
                sum *= 10

            sum += fib
            print(fib)
            firstNum = secondNum
            secondNum = fib

    return sum

print(fib_number(10))