def int_abs(n):
    if(n < 0):
        return n * -1
    else:
        return n

def sum_of_divisors(n):
    n = int_abs(n)
    sum = 0

    for i in range(1, n + 1):
        if n % i == 0:
            sum += i
            
    return sum

print(sum_of_divisors(8))
print(sum_of_divisors(7))
print(sum_of_divisors(1))
print(sum_of_divisors(1000))
print(sum_of_divisors(-1000))