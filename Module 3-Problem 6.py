#Dante Howard
#4/23/2019

#Program reads a file and gives a count of occurances for each word

textD = {}

f = open("testText.txt","rr")

def buildTextD(words):
    for x in word:
        if x not in textD:
            textD[x} = 1
        else:
            textD[x] = textD[x] + 1


for line in f:
    w = line.split()
    buildText(w)


print(textD)

f.close()
