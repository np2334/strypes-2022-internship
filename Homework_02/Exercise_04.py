def get_number_length(n):
    length = 0
    while n != 0:
        n //= 10
        length += 1
    return length 

def reverse_int(n):
    reversedInt = 0
    while n != 0:
        reversedInt += n % 10
        reversedInt *= 10
        n //= 10
    reversedInt //= 10
    return reversedInt

def is_int_palindrome(n):
    numberLength = get_number_length(n)
    isEven = numberLength % 2 == 0
    switchHalf = False

    firstHalf = 0
    secondHalf = 0
    for i in range(0, numberLength):
        if not isEven and i == numberLength // 2:
            n //= 10
            switchHalf = True
            continue

        currentNumber = n % 10
        n //= 10

        if switchHalf:
            firstHalf += currentNumber
            firstHalf *= 10
        else:
            secondHalf += currentNumber
            secondHalf *= 10

        if isEven and i == numberLength // 2 - 1:
            switchHalf = True
    
    firstHalf //= 10
    secondHalf //= 10

    print(firstHalf)
    print(secondHalf)

    # тук имах проблем ако първото число за дадената половина е 0, в този случай след неговото умножаване по 10 остава 0 и не мога да долепя следващи числа или самата 0 преди следващото числото
    # примерно при 100001 като половини се получават 1 (firstHalf) и 100 (secondHalf) вместо 001 и 100, затова вече обръщам secondHalf, защото няма как числото да е огледално и да започва с 0  
    # firstHalf = reverse_int(firstHalf)
    secondHalf = reverse_int(secondHalf)

    if firstHalf == secondHalf: 
        return True
    else:
        return False

print(is_int_palindrome(101000101))
print(is_int_palindrome(1))
print(is_int_palindrome(42))
print(is_int_palindrome(100001))
print(is_int_palindrome(999))
print(is_int_palindrome(123))
print(is_int_palindrome(123456))
print(is_int_palindrome(123321))
print(is_int_palindrome(11511))
print(is_int_palindrome(22222222222222))