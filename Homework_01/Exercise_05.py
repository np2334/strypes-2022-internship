def int_abs(n):
    if n < 0:
        n *= -1
    return n

def get_number_length(n):
    length = 0
    while n != 0:
        n //= 10
        length += 1
    return length

def is_number_balanced(n):
    n = int_abs(n)
    numberLength = get_number_length(n)

    if numberLength == 1:
        return True

    isOdd = numberLength % 2 != 0

    firstHalf = 0
    secondHalf = 0
    switchHalf = False
    for i in range(0, numberLength):
        # ако числото е нечетно и съм стигнал средата му пропускам числото и започвам да добавям към другата половина
        if isOdd and i == (numberLength // 2):
            switchHalf = True
            n //= 10
            continue
        
        currentNumber = n % 10
        
        if switchHalf:
            firstHalf += currentNumber
        else:
            secondHalf += currentNumber

        n //= 10

        # ако числото е четно и съм минал първата половина (примерно за 4 числа от индекс 0 до 3 => 4 // 2 = 2 - 1 (заради индексирането от 0) = 1 индекс е края на първата половина)
        if not isOdd and i == (numberLength // 2) - 1:
            switchHalf = True

    if firstHalf == secondHalf:
        return True
    else:
        return False
        

print(is_number_balanced(-2))
print(is_number_balanced(13003))
print(is_number_balanced(13031))
print(is_number_balanced(111210))
print(is_number_balanced(123210))
print(is_number_balanced(28471))
print(is_number_balanced(1238033))


    

