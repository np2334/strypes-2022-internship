def is_anagram(fst_word, snd_word):
    if len(fst_word) != len(snd_word):
        return False

    fst_word = sorted(fst_word.lower())
    snd_word = sorted(snd_word.lower())

    # for i in range(0, len(fst_word)):
    #     first_character = fst_word[i]
    #     second_character = snd_word[i]

    #     if first_character != second_character:
    #         return False
    # return True

    if fst_word == snd_word:
        return True
    return False



print(is_anagram("BRADE", "BeaRD"))
print(is_anagram("TOP_CODER", "COTO_PRODE"))


 