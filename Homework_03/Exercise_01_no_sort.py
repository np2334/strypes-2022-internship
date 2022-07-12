def is_index_contained(array, value):
    for element in array:
        if element == value:
            return True
    return False

# разглеждам ги като ASCII кодове
# a = 97, A = 65 => 97 - 65 = 32, т.е. ако имам 66 'B' добавям 32 и получавам 98 'b'
def to_lower(character):
    return chr(ord(character) + 32) if ord(character) in range(65, 91) else character

def is_anagram(fst_word, snd_word):
    needed_characters = 0
    foundIndexes = []

    for i in range(0, len(fst_word)):
        first_word_character = to_lower(fst_word[i])

        for j in range(0, len(snd_word)):
            if not is_index_contained(foundIndexes, j):
                second_word_character = to_lower(snd_word[j])

                if first_word_character == second_word_character:
                    needed_characters += 1
                    foundIndexes.append(j)
                    break
    
    print(needed_characters)
    if needed_characters == len(fst_word) and len(fst_word) == len(snd_word):
        return True
    return False

print(is_anagram("BRADE", "BeaRD"))
print(is_anagram("TOP_CODER", "COTO_PRODE"))

