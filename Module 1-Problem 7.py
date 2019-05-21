#Dante Howard
#4/23/2019

#Problem 7 this will give you the sum of the positive numbers then subtract the negative odd

answer = 0

n = [2, -25, 32, -13, 56, -9, 26, -31]

for element in n:
    if element %2 == 0 and element > 0:
        answer += element
    elif element %2 == 1 and element < 0:
        answer -= element

print (answer)
