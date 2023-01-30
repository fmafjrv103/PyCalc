# Calculater

import numpy as np# For "others" option

# Constants
# Constants for output
p = " plus "
s = " minus "
d = " divided by "
m = " times "
e = " is equal to "
# Constants for input
en = "Enter number: "
n = "How Many Numbers?(1-5): "
# Warnings
warn0 = "Do you want to exit?(y or n): "
warn1 = "Are you sure you want to exit?(y or n): "
# Errors
error0 = "Try again"
error1 = "Invalid Input, Please try again"

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
exit = False
while exit is False:
    print("1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Other\n6) Credits\n7) Exit")# Menu

    # Input for Menu
    selectItem = int(input("Pick: ")) # I only want number as it is easier

    # Menu
    # Addition
    exit0 = False
    if selectItem == 1:
        while exit0 is False:
            print("You picked Addition")
            amountNum = int(input(n))# Allows user to pick how many numbers they want to add(only up to 5)
            num = "You have ",amountNum," Numbers"# Constant for numbers

            # Adding of two intagers
            if amountNum == 2:
                numArray = [0,0]# Array used to store numbers inputed by user
                index = 0
                print(num)
                while index < len(numArray):
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0] + numArray[1]# Output
                print(numArray[0], p, numArray[1], e, out, "\n")# Printed Output
                while exit0 is False:
                    out0 = input(warn0)
                    if out0 == "y":
                        exit0 = True
                    elif out0 == "n":
                        break
                    else:
                        print(error0)

            # Adding of three intagers
            elif amountNum == 3:
                numArray = [0,0,0]
                index = 0
                print(num)
                while index < len(numArray):
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0] + numArray[1] + numArray[2]# Output
                print(numArray[0], p, numArray[1], p, numArray[2], e, out, "\n")# Printed Output
                while exit0 is False:
                    out0 = input(warn0)
                    if out0 == "y":
                        exit0 = True
                    elif out0 == "n":
                        break
                    else:
                        print(error0)

            # Adding of four intagers
            elif amountNum == 4:
                numArray = [0,0,0,0]
                index = 0
                print(num)
                while index < len(numArray):
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0] + numArray[1] + numArray[2] + numArray[3]# Output
                print(numArray[0], p, numArray[1], p, numArray[2], p, numArray[3], e, out, "\n")# Printed Output
                while exit0 is False:
                    out0 = input(warn0) 
                    if out0 == "y":
                        exit0 = True
                    elif out0 == "n":
                        break
                    else:
                        print(error0)

            # Adding of five intagers
            elif amountNum == 5:
                numArray = [0,0,0,0,0]
                index = 0
                print(num)
                while index < len(numArray):
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0] + numArray[1] + numArray[2] + numArray[3] + numArray[4]# Output
                print(numArray[0], p, numArray[1], p, numArray[2], p, numArray[3], p, numArray[4], e, out, "\n")# Printed Output
                while exit0 is False:
                    out0 = input(warn0)
                    if out0 == "y":
                        exit0 = True
                    elif out0 == "n":
                        break
                    else:
                        print(error0)
            else:
                print(error1)

    # Subtracting
    elif selectItem == 2:
        while exit0 is False:
            print("You picked Subtraction")
            amountNum = int(input(n))# Allows user to pick how many numbers they want to add(only up to 5)

            # Subtracting of two intagers
            if amountNum == 2:
                numArray = [0,0]# Array used to store numbers inputed by user
                index = 0
                print(num)
                while index < len(numArray):
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0] - numArray[1]# Output
                print(numArray[0], s, numArray[1], e, out, "\n")# Printed Output
                while exit0 is False:
                    out0 = input(warn0)
                    if out0 == "y":
                        exit0 = True
                    elif out0 == "n":
                        break
                    else:
                        print(error0)

            # Subtracting of three intagers
            elif amountNum == 3:
                numArray = [0,0,0]
                index = 0
                print(num)
                while index < len(numArray):
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0] - numArray[1] - numArray[2]# Output
                print(numArray[0], s, numArray[1], s, numArray[2], e, out, "\n")# Printed Output
                while exit0 is False:
                    out0 = input(warn0)
                    if out0 == "y":
                        exit0 = True
                    elif out0 == "n":
                        break
                    else:
                        print(error0)

            # Subtracting of four intagers
            elif amountNum == 4:
                numArray = [0,0,0,0]
                index = 0
                print(num)
                while index < len(numArray):
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0] - numArray[1] - numArray[2] - numArray[3]# Output
                print(numArray[0], s, numArray[1], s, numArray[2], s, numArray[3], e, out, "\n")# Printed Output
                while exit0 is False:
                    out0 = input(warn0)
                    if out0 == "y":
                        exit0 = True
                    elif out0 == "n":
                        break
                    else:
                        print(error0)

            # Subtracting of five intagers
            elif amountNum == 5:
                numArray = [0,0,0,0,0]
                index = 0
                print(num)
                while index < len(numArray):
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0] - numArray[1] - numArray[2] - numArray[3] - numArray[4]# Output
                print(numArray[0], s, numArray[1], s, numArray[2], s, numArray[3], s, numArray[4], e, out, "\n")# Printed Output
                while exit0 is False:
                    out0 = input(warn0)
                    if out0 == "y":
                        exit0 = True
                    elif out0 == "n":
                        break
                    else:
                        print(error0)
            else:
                print(error1)

    # Multipication
    elif selectItem == 3:
        while exit0 is False:
            print("You picked Multiplication")
            amountNum = int(input(n))# Allows user to pick how many numbers they want to add(only up to 5)

            # Multiplying of two intagers
            if amountNum == 2:
                numArray = [0,0]# Array used to store numbers inputed by user
                index = 0
                print(num)
                while index < len(numArray):
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0] * numArray[1]# Output
                print(numArray[0], m, numArray[1], e, out, "\n")# Printed Output
                while exit0 is False:
                    out0 = input(warn0)
                    if out0 == "y":
                        exit0 = True
                    elif out0 == "n":
                        break
                    else:
                        print(error0)

            # Muliplying of three intagers
            elif amountNum == 3:
                numArray = [0,0,0]
                index = 0
                print(num)
                while index < len(numArray):
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0] * numArray[1] * numArray[2]# Output
                print(numArray[0], m, numArray[1], m, numArray[2], e, out, "\n")# Printed Output
                while exit0 is False:
                    out0 = input(warn0)
                    if out0 == "y":
                        exit0 = True
                    elif out0 == "n":
                        break
                    else:
                        print(error0)

            # Multiplying of four intagers
            elif amountNum == 4:
                numArray = [0,0,0,0]
                index = 0
                print(num)
                while index < len(numArray):
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0] * numArray[1] * numArray[2] * numArray[3]# Output
                print(numArray[0], m, numArray[1], m, numArray[2], m, numArray[3], e, out, "\n")# Printed Output
                while exit0 is False:
                    out0 = input(warn0)
                    if out0 == "y":
                        exit0 = True
                    elif out0 == "n":
                        break
                    else:
                        print(error0)

            # Multiplying of five intagers
            elif amountNum == 5:
                numArray = [0,0,0,0,0]
                index = 0
                print(num)
                while index < len(numArray):
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0] * numArray[1] * numArray[2] * numArray[3] * numArray[4]# Output
                print(numArray[0], m, numArray[1], m, numArray[2], m, numArray[3], m, numArray[4], e, out, "\n")# Printed Output
                while exit0 is False:
                    out0 = input(warn0)
                    if out0 == "y":
                        exit0 = True
                    elif out0 == "n":
                        break
                    else:
                        print(error0)
            else:
                print(error1)

    # Division
    elif selectItem == 4:
        while exit0 is False:
            print("You picked Division")
            amountNum = int(input(n))# Allows user to pick how many numbers they want to add(only up to 5)

            # Dividing of two intagers
            if amountNum == 2:
                numArray = [0,0]# Array used to store numbers inputed by user
                index = 0
                print(num)
                while index < len(numArray):
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0] / numArray[1]# Output
                print(numArray[0], d, numArray[1], e, out, "\n")# Printed Output
                while exit0 is False:
                    out0 = input(warn0)
                    if out0 == "y":
                        exit0 = True
                    elif out0 == "n":
                        break
                    else:
                        print(error0)

            # Dividin/ of three intagers
            elif amountNum == 3:
                numArray = [0,0,0]
                index = 0
                print(num)
                while index < len(numArray):
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0] / numArray[1] / numArray[2]# Output
                print(numArray[0], d, numArray[1], d, numArray[2], e, out, "\n")# Printed Output
                while exit0 is False:
                    out0 = input(warn0)
                    if out0 == "y":
                        exit0 = True
                    elif out0 == "n":
                        break
                    else:
                        print(error0)

            # Dividing of four intagers
            elif amountNum == 4:
                numArray = [0,0,0,0]
                index = 0
                print(num)
                while index < len(numArray):
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0] / numArray[1] / numArray[2] / numArray[3]# Output
                print(numArray[0], d, numArray[1], d, numArray[2], d, numArray[3], e, out, "\n")# Printed Output
                while exit0 is False:
                    out0 = input(warn0)
                    if out0 == "y":
                        exit0 = True
                    elif out0 == "n":
                        break
                    else:
                        print(error0)

            # Dividing of five intagers
            elif amountNum == 5:
                numArray = [0,0,0,0,0]
                index = 0
                print(num)
                while index < len(numArray):
                    numArray[index] = int(input(en))
                    index += 1
                out = numArray[0] / numArray[1] / numArray[2] / numArray[3] / numArray[4]# Output
                print(numArray[0], d, numArray[1], d, numArray[2], d, numArray[3], d, numArray[4], e, out, "\n")# Printed Output
                while exit0 is False:
                    out0 = input(warn0)
                    if out0 == "y":
                        exit0 = True
                    elif out0 == "n":
                        break
                    else:
                        print(error0)
            else:
                print(error1)

    # Other
    elif selectItem == 5:
        while exit0 is False:
            print("Scientific options will be coming sone as full version comes out")
            exit0 = True

    # Credits
    elif selectItem == 6:
        while exit0 is False:
            print("Made By: Fmafjrv103")
            print("   Github: https://github.com/fmafjrv103")
            print("Lisenced under: MIT")
    # Exit
    elif selectItem == 7:
        while exit0 is False:
            out1 = input(warn1)
            if out1 == "y":
                exit0 = True
                exit = True
            elif out1 == "n":
                break
            else:
                print(error0)