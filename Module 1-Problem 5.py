#Dante Howard
#04/23/2019

#Problem 5 this will give you a list of unique elements out of a list.

numbers = [1,3,3,3,6,2,3,5]

un = []
for n in numbers:
    if n not in un:
        un.append(n)

print (un)
