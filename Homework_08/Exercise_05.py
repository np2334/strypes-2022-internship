def func():
    number_one = 0
    with open("numbers.txt", "r") as reader:
            number_one = reader.readline()[:-1]

            number_expression = reader.readline()[:-1]
            try:
                while number_expression != "":
                    number_one = eval("{} {}".format(number_one, number_expression))
                    number_expression = reader.readline()[:-1]   
            except:
                pass
    return number_one      

print(func())