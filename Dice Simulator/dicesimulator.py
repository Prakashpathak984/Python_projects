import random

x = "y"
while x == "y":
    num = random.randint(1,6)
    if num == 1:
        print("-------------")
        print("|           |")
        print("|     0     |")
        print("|           |")
        print("-------------")
    elif num == 2:
        print("-------------")
        print("|           |")
        print("|   0   0   |")
        print("|           |")
        print("-------------")
    elif num == 3:
        print("-------------")
        print("|     0     |")
        print("|     0     |")
        print("|     0     |")
        print("-------------")
    elif num == 4:
        print("-------------")
        print("|  0     0  |")
        print("|           |")
        print("|  0     0  |")
        print("-------------")
    elif num == 5:
        print("-------------")
        print("|  0     0  |")
        print("|     0     |")
        print("|  0     0  |")
        print("-------------")
    elif num == 6:
        print("-------------")
        print("|  0     0  |")
        print("|  0     0  |")
        print("|  0     0  |")
        print("-------------")
    x = input("Press y to roll again : ")
