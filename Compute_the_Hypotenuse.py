#importing math
import math

#defining pythagorean theorem function
def pythagorean_theorem(side_a, side_b):
    hypotenuse = math.sqrt(side_a**2 + side_b**2)
    return hypotenuse

#receiving input from user
side_a = input("Please input Side A: ")
if side_a.isalpha() == True:
    print("Please input a positive number.")
    exit()
elif float(side_a) <= 0:
    print("Please input a positive number.")
    exit()
else:
    side_a = float(side_a)

side_b = input("Please input Side B: ")
if side_b.isalpha() == True:
    print("Please input a positive number.")
    exit()
elif float(side_b) <= 0:
    print("Please input a positive number.")
    exit()
else:
    side_b = float(side_b)

#printing result
print("The hypotenuse is", str(pythagorean_theorem(side_a, side_b)), "units long.")

