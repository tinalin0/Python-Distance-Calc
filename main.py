# Python Distance Calc
import math

print("WELCOME TO THE DISTANCE CALCULATOR!")

# Input
x1 = float(input("\nEnter x1 value: "))
y1 = float(input("Enter y1 value: "))
x2 = float(input("Enter x2 value: "))
y2 = float(input("Enter y2 value: "))

# Process
distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)

# Output
print("\nDistance between the two points is " + str(distance) + ".")
