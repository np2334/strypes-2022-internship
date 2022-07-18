def roman_to_integer(roman_number_string):
    roman_numerals = {
        'I': 1, 
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    sum = 0
    i = 0
    while i < len(roman_number_string):
        if True:
            currentCharacter = roman_number_string[i]
            nextCharacterIndex = i + 1

        if nextCharacterIndex < len(roman_number_string):
            if currentCharacter == 'I' and (roman_number_string[nextCharacterIndex] == 'V' or roman_number_string[nextCharacterIndex] == 'X'):
                sum += roman_numerals[roman_number_string[nextCharacterIndex]] - roman_numerals[currentCharacter]
                i += 2
                continue
            elif currentCharacter == 'X' and (roman_number_string[nextCharacterIndex] == 'L' or roman_number_string[nextCharacterIndex] == 'C'):
                sum += roman_numerals[roman_number_string[nextCharacterIndex]] - roman_numerals[currentCharacter]
                i += 2
                continue
            elif currentCharacter == 'C' and (roman_number_string[nextCharacterIndex] == 'D' or roman_number_string[nextCharacterIndex] == 'M'):
                sum += roman_numerals[roman_number_string[nextCharacterIndex]] - roman_numerals[currentCharacter]
                i += 2
                continue
        sum += roman_numerals[currentCharacter]
        i += 1
    return sum

s = "III"
print(roman_to_integer(s))

s = "LVIII"
print(roman_to_integer(s))

s = "MCMXCIV"
print(roman_to_integer(s))