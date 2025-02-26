# Author: Conor Kelly
# Date: February 25, 2025  
# This program uses variables, math operations, discriminant calculations, and 3D volume calculations

import math

# Variable Types

integer = 10  
float_ = 10.5  
precise_float = 10.5555555555
char = 'A'
boolean = True  
string = "Hello"  

# Print the values with their explanations

print("\nVariable Type Examples")
print("\nThis is an example of a Integer Variable:", integer)
print("This is an example of a Float Variable:", float_)
print("This is an example of a Precise Float Variable:", precise_float)
print("This is an example of a Char Variable:", char)
print("This is an example of a Boolean Variable:", boolean)
print("This is an example of a String Variable:", string)

# Math Operations

add = 2 + 23
difference = 2 - 23
multiply = 3 * 2 * 4
divide = 24 // 8 
divide_float = 24.0 / 7  
square = math.sqrt(25)
power = 2 ** 4
rem_1 = 24 % 6
rem_2 = 24 % 5
rem_3 = 24 % 7

# Printing the results

print("\nMath Operations Stored in Variables:")
print("\nAddition (2 + 23):", add)
print("Subtraction (2 - 23):", difference)
print("Product (3 * 2 * 4):", multiply)
print("Quotient Integer (24 / 8):", divide)
print("Quotient Float (24.0 / 7):", divide_float)
print("Square Root (math.sqrt(25)):", square)
print("Exponentiation (2 ** 4):", power)
print("Modulus 1 (24 % 6):", rem_1)
print("Modulus 2 (24 % 5):", rem_2)
print("Modulus 3 (24 % 7):", rem_3)

# Discriminant Calculator 

print("\nDiscriminant Calculator")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

delta = b ** 2 - 4 * a * c

print("\nDiscriminant:", delta)

# 3D Volume Calculator

# Cube Calculator

side = float(input("\nEnter the side length of the cube: "))
cube_volume = side ** 3
print("Volume of the cube:", cube_volume)

# Sphere Calculator
sphere_radius = float(input("Enter the radius of the sphere: "))
sphere_volume = (4/3) * math.pi * sphere_radius ** 3
print("Volume of the sphere:", sphere_volume)

# Cone Calculator
cone_radius = float(input("Enter the radius of the cone: "))
cone_height = float(input("Enter the height of the cone: "))
cone_volume = (1/3) * math.pi * cone_radius ** 2 * cone_height
print("Volume of the cone:", cone_volume)

# Cylinder Calculator
cylinder_radius = float(input("Enter the radius of the cylinder: "))
cylinder_height = float(input("Enter the height of the cylinder: "))
cylinder_volume = math.pi * cylinder_radius ** 2 * cylinder_height
print("Volume of the cylinder:", cylinder_volume)
