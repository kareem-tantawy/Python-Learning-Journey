# ------------------------ #
# -- Function Recursion -- #
# ------------------------ #


def factorail(n):
    if n == 1:
        return n
    else: return n * factorail(n-1)
    
print(factorail(5))


def cleanWord(word):
    if len(word) == 1:
        return word
    if word[0] == word[1]:
        return cleanWord(word[1:])
    else:
        return word[0] + cleanWord(word[1:])
    

print(cleanWord("KKKKaaarriim"))