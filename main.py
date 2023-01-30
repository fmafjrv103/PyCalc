# Calculater

import numpy as np

# Constants
p = " plus "
m = " minus "
d = " divided by "
m = " times "
e = " is equal to "
en = "Enter number: "

# Basic interface
print("$$$$$$$\             $$$$$$\            $$\           ")
print("$$  __$$\           $$  __$$\           $$ |          ")
print("$$ |  $$ |$$\   $$\ $$ /  \__| $$$$$$\  $$ | $$$$$$$\ ")
print("$$$$$$$  |$$ |  $$ |$$ |       \____$$\ $$ |$$  _____|")
print("$$  ____/ $$ |  $$ |$$ |       $$$$$$$ |$$ |$$ /      ")
print("$$ |      $$ |  $$ |$$ |  $$\ $$  __$$ |$$ |$$ |      ")
print("$$ |      \$$$$$$$ |\$$$$$$  |\$$$$$$$ |$$ |\$$$$$$$\ ")
print("\__|       \____$$ | \______/  \_______|\__| \_______|")
print("          $$\   $$ |  By: Fmafjrv103                  ")
print("          \$$$$$$  |  https://github.com/fmafjrv103/PyCalc ")
print("           \______/                                   ")
print("\n")
print("What do you want to do:\n")

# Printed Menu
print("1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Other\n6) Credits")

# Input for Menu
selectItem = int(input("Pick: ")) # I only want number as it is easier

# Menu
# Addition
exit = False
while exit is False:
    if selectItem == 1:
        exit0 = False
        while exit0 == 0:
            print("You picked Addition")
            amountNum = int(input("how many numbers?(2-5): "))# Allows user to pick how many numbers they want to add(only up to 5)
            num = "You have ",amountNum," Numbers"# Constant for numbers
            if amountNum == 2:
                numArray = [0,0]# Array used to store numbers inputed by user
                index = 0
                print(num)
                while index < len(numArray):
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0] + numArray[1]
                print(numArray[0],p,numArray[1],e,out,"\n")
                exit0 = input("Would you like to exit(y or n): ")
                if exit0 == "y":
                    exit0 = 1
                else:
                    exit0 = 0
            elif amountNum == 3:
                numArray = [0,0,0]
                index = 0
                while index < len(numArray):
                    print(num)
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0]+numArray[1]+numArray[2]
                print(numArray[0],p,numArray[1],p,numArray[2],e,out)
            elif amountNum == 4:
                numArray = [0,0,0,0]
                index = 0
                while index < len(numArray):
                    print(num)
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0]+numArray[1]+numArray[2]+numArray[3]
                print(numArray[0],p,numArray[1],p,numArray[2],p,numArray[3],e,out)
            elif amountNum == 5:
                numArray = [0,0,0,0,0]
                index = 0
                while index < len(numArray):
                    print(num)
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0]+numArray[1]+numArray[2]+numArray[3]+numArray[4]
                print(numArray[0],p,numArray[1],p,numArray[2],p,numArray[3],p,numArray[4],e,out)
            else:
                print("Invalid Input, Please try again")