def int_abs(n):
    if(n < 0):
        return n * -1
    else:
        return n

def is_prime(n):
    if n == 1: return False

    n = int_abs(n)
    for i in range(1, n + 1):
        if n % i == 0 and i != 1 and i != n:
            return False
    return True

print(is_prime(1))
print(is_prime(2))
print(is_prime(8))
print(is_prime(11))
print(is_prime(-10))