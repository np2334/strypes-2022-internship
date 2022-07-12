# отново взимам ASCII кода и проверяввам дали е число според него (от 48 до 57 са цифрите)
def is_digit(character):
    return ord(character) in range(48, 58)

# 48 - 48 = 0, 49 - 48 = 1, 50 - 48 = 2 и т.н.
def character_digit_to_number(digit):
    return ord(digit) - 48

def sum_of_numbers(input):
    digitFound = False
    sum = 0
    # понеже string-a е immutable вместо да правя нов string в паметта всеки път щом го променя 
    # реших да ползвам цяло число, така използвам аритметични операции и би трябвало да е по-бързо
    num = 0 

    for character in input:
        if is_digit(character):
            num += character_digit_to_number(character)
            num *= 10
        else:
            num //= 10
            sum += num
            num = 0

    if num != 0:
        num //= 10
        sum += num
        
    return sum

print(sum_of_numbers("ab125cd3"))
print(sum_of_numbers("ab12"))
print(sum_of_numbers("ab"))
print(sum_of_numbers("123ab"))
print(sum_of_numbers("44s2"))