def nan_expand(times):
    #'"' escape-ва кавички 
    output = "\""

    for i in range(0, times):
        output += "Not a " 
    if times != 0:
        output += "NaN"

    return output + "\""

print(nan_expand(0))
print(nan_expand(1))
print(nan_expand(2))
print(nan_expand(3))