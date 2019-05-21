#Dante Howard
#4/23/2019

WordList = [1,2,3,4,5]
def reverse(words):
    return [words[-1]] + reverse(words[:-1]) if words else []

print(reverse(WordList))
