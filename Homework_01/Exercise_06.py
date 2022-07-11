def is_decreasing(seq):
    lastElement = seq[0]
    for i in range(1, len(seq)):
        currentElement = seq[i]
        if currentElement >= lastElement:
            return False
        lastElement = currentElement
    return True
        
print(is_decreasing([5, 4, 3, 2, 1]))
print(is_decreasing([5, 4, 8, 2, 1]))
print(is_decreasing([1, 2, 3]))
print(is_decreasing([1, 1, 1, 1]))
print(is_decreasing([100, 50, 20]))

