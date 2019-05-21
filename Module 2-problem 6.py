#Dante Howard
#04/23/2019

#program will count the number of times each letter shows up in a string

s = "a, e, i, o, u, get, appeared"

d = {}

for x in 'abcdefghijklmnopqustuvwxyz':
    d[x] = 0

for letter in s:
    if letter in d:
        d[letter] += 1
print(d)
