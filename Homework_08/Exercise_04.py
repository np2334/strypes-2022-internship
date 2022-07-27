def func(number):
    number_one = number
    while(True):
        try:
            num_operation = input() # + - * / 
            number_two = input() # num 

            # TODO match
            number_one = eval("{} {} {}".format(number_one, num_operation, number_two))
        except:
            break
    return number_one

print(func(0))