# Dante Jackson
# 3/7/19

# Checks if two user inputs are equal


number1 = int(input("Enter in number 1: "))
number2 = int(input("Enter in number 2: "))
def numbercheck(nl, n2):
    if nl == n2:
        print("true")
        return True
    else:
        print("false")
        return False

numbercheck(number1, number2)
print(numbercheck(number1, number2))
