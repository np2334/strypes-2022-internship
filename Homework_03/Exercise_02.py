def is_anagram(fst_word, snd_word):
    needed_characters = 0
    for i in range(0, len(fst_word)):
        first_word_character = fst_word[i].lower()

        for j in range(0, len(snd_word)):
            second_word_character = snd_word[i].lower()

            if first_word_character == second_word_character:
                needed_characters += 1
    
    print(needed_characters)
    if needed_characters == len(fst_word):
        return True
    return False

print(is_anagram("BRADE", "BeaRD"))
print(is_anagram("TOP_CODER", "COTO_PRODE"))

