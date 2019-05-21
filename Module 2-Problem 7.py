#Dante Howard
#04/23/2019

#Problem 7 this program will open a file and if it's not there it will make an exception.


try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError:
    print("File not Found")
