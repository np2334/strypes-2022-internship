def nan_expand(times):
    output = ""

    for i in range(0, times):
        output += "Not a " 
    if times != 0:
        output += "NaN"

    if times == 0:
        #'"' escape-ва кавички 
        return "\"\""
    return output


print(nan_expand(0))
print(nan_expand(1))
print(nan_expand(2))
print(nan_expand(3))