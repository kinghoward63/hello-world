#Dante Howard
#04/23/2019

#This program will give python interpreter's for a continuous session.

def add_fruit(inventory, fruit, quantity):
    inventory[fruit] = quantity
    




new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
if 'strawberries' in new_inventory:
    print("yes. 'Strawberries' is a key")
if new_inventory ['strawberries'] == 10:
    print("There are 10 Strawberries")

add_fruit(new_inventory, 'grapes', 25)
if 'grapes' in new_inventory:
    print("yes. 'grapes' is a key")
if new_inventory ['grapes'] == 25:
    print("There are 25 grapes.")
