def sum_of_numbers(input):
    sum = 0
    num = ""
    
    for character in input:
        # TODO define isdigit function
        if character.isdigit():
            num += character
        else:
            if num != "":
                sum += int(num)
                num = ""

    # ако е останало от последната итерация
    if num != "":
        sum += int(num)

    return sum

print(sum_of_numbers("ab125cd3"))
print(sum_of_numbers("ab12"))
print(sum_of_numbers("ab"))
print(sum_of_numbers("123ab"))
print(sum_of_numbers("44s2"))