def is_anagram(fst_word, snd_word):
    if len(fst_word) != len(snd_word):
        return False

    fst_word = sorted(fst_word.lower())
    snd_word = sorted(snd_word.lower())

    if fst_word == snd_word:
        return True
    return False

print(is_anagram("BRADE", "BeaRD"))
print(is_anagram("TOP_CODER", "COTO_PRODE"))


 