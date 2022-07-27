# type error
# 0
def divide_positive_numbers(a, b):
    result = 0
    try:
        if a < 0 or b < 0:
            raise ValueError()
        result = a / b
    except ZeroDivisionError:
        print("Zero division is not possible.")
    except TypeError:
        print("Invalid type - expected number.")
    except ValueError:
        print("Negative numbers not allowed.")
    else:
        return result

print(divide_positive_numbers(5, 0))
print(divide_positive_numbers(5, "asdasd"))
print(divide_positive_numbers(5, -5))
print(divide_positive_numbers(5, 5))




