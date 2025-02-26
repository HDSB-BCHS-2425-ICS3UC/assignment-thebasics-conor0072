# Author: Conor Kelly
# Date: February 25, 2025  
# This program uses variables, math operations, discriminant calculations, and 3D volume calculations

import math

# Variable Types

integer = 10  
float = 10.5  
double = 10.5555555555
char = 'A'
boolean = True  
string = "Hello"  

# Print the values with their explanations

print("\nVariable Type Examples")
print("\nThis is an example of a Integer Variable:", str(integer))
print("This is an example of a Float Variable:", str(float))
print("This is an example of a Double Variable:", str(double))
print("This is an example of a Char Variable:", char)
print("This is an example of a Boolean Variable:", str(boolean))
print("This is an example of a String Variable:", string)

# Math Operations

add = 2 + 23
difference = 2 - 23
multiply = 3 * 2 * 4
divide = 24 / 8
divide_float = 24.0 / 7  
square = math.sqrt(25)
power = 2 ** 4
rem_1 = 24 % 6
rem_2 = 24 % 5
rem_3 = 24 % 7

# Printing the results

print("\nMath Operations Stored in Variables:")
print("\nAddition (2 + 23):", str(add))
print("Subtraction (2 - 23):", str(difference))
print("Product (3 * 2 * 4):", str(multiply))
print("Quotient Integer (24 / 8):", str(divide))
print("Quotient Float (24.0 / 7):", str(divide_float))
print("Square Root (math.sqrt(25)):", str(square))
print("Exponentiation (2 ** 4):", str(power))
print("Modulus 1 (24 % 6):", str(rem_1))
print("Modulus 2 (24 % 5):", str(rem_2))
print("Modulus 3 (24 % 7):", str(rem_3))

# Discriminant Calculator 

print("\nDiscriminant Calculator")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

delta = b * b - 4 * a * c

print("\nDiscriminant:", delta)

# 3D Volume Calculator

# Cube Calculator

side = int(input("\nEnter the side length of the cube: "))
cube_volume = side ** 3
print("Volume of the cube:", cube_volume)

# Sphere Calculator
radius = int(input("Enter the radius of the sphere: "))
sphere_volume = (4/3) * 3.14159 * radius ** 3
print("Volume of the sphere:", sphere_volume)

# Cone Calculator
radius = int(input("Enter the radius of the cone: "))
height = int(input("Enter the height of the cone: "))
cone_volume = (1/3) * 3.14159 * radius ** 2 * height
print("Volume of the cone:", cone_volume)

# Cylinder Calculator
radius = int(input("Enter the radius of the cylinder: "))
height = int(input("Enter the height of the cylinder: "))
cylinder_volume = 3.14159 * radius ** 2 * height
print("Volume of the cylinder:", cylinder_volume)
