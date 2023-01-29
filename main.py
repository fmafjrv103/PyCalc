# Calculater

import numpy as np

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
if selectItem == 1:
    print("You picked Addition")
    amountNum = int(input("how many numbers?(2-5): "))# Allows user to pick how many numbers they want to add(only up to 5)
    if amountNum == 2:
        index = 0
        print("You have 2 numbers")
        while index < 2:
            num0 = int(input("Enter number: "))