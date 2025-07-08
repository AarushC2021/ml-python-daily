def cap(word) :
    if not word :
        return ""
    return word[0].upper() + word[1:]
word = input().strip()
print(cap(word))