def is_number_contained(array, wantedNumber):
    for number in array:
        if number == wantedNumber:
            return True
    return False

# skipIndexArray е масив с индекси, които са вече намерени и искам да бъдат пропуснати, за да мога да продължа напред с итерацията върху string-a
# има default-на стойност -1 за да може да влезе във for-a и да върне индекс ако се извика функцията без стойности за този масив (примерно find_index_of("aabaa", "b", 0))
def find_index_of(input, character, startIndex, skipIndexArray = [ -1 ]):
    for i in range(startIndex, len(input)):
        if input[i] == character and not is_number_contained(skipIndexArray, i):
                return i
    return -1

def count_substring(input, wantedString):
    index = find_index_of(input, wantedString[0], 0)
    count = 0
    foundIndexes = []

    if index == -1: return 0

    lastFoundIndex = 0
    while index != -1:
        foundIndexes.append(index)

        isFullMatch = True
        for i in range(0, len(wantedString)):
            # ако имаме "baba ba" и търсим "ba" ще даде out of range, защото намирам 3 пъти b
            # и от последното b string-a е само "ba" а аз итерирам колкото е търсения string т.е. "baba"
            if index + i > len(input) - 1:
                return count

            if input[index + i] != wantedString[i]:
                isFullMatch = False
                break
            
        if isFullMatch:
            lastFoundIndex = index + len(wantedString) - 1; 
            count += 1
        
        # тук ми се наложи да добавя и startIndex към find_index_of заради примера с "babababa" за да мога да започна да търся след края на вече намерената дума
        # в противен случай намирам 3 пъти baba
        index = find_index_of(input, wantedString[0], lastFoundIndex + 1, foundIndexes)
    
    return count

print(count_substring("This is a test string", "is"))
print(count_substring("babababa", "baba"))
print(count_substring("Python is an awesome language to program in!", "o"))
print(count_substring("We have nothing in common!", "really"))
print(count_substring("This is this and that is this", "this"))
print(count_substring("baba ba", "baba"))