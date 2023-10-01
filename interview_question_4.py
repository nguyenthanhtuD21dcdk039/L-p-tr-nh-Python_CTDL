def is_anagram(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")

    if len(s1) != len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 == s2:
        return True

    return False


word1 = "restful"
word2 = "fluster"

if is_anagram(word1, word2):
    print(word1, "và", word2, "là anagram.")
else:
    print(word1, "và", word2, "không phải là anagram.")
