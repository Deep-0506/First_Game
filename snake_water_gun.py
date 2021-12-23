import random

def game(computer_value , yours_value):
    if(computer_value == yours_value):
        return None
    elif(computer_value == "s"):
        if(yours_value == "w"):
            return False
        elif(yours_value == "g"):
            return True
    elif(computer_value == "w"):
        if(yours_value == "g"):
            return False
        elif(yours_value == "s"):
            return True
    elif(computer_value == "g"):
        if(yours_value == "s"):
            return False
        elif(yours_value == "w"):
            return True



print("Computer's turn : Choose from Snake(s) , Water(w) , Gun(g)")
yours_value = input("Your's turn : Choose from Snake(s) , Water(w) , Gun(g) = ")

a = random.randint(1,3)

if(a == 1):
    computer_value = "s"
elif(a == 2):
    computer_value = "w"
else:
    computer_value = "g"

print("Computer choose : ",computer_value)
print("You Choose : ",yours_value)

b = game(computer_value,yours_value)

if(b == None):
    print("Game is tie")
elif(b):
    print("You Win")
else:
    print("You Lose")