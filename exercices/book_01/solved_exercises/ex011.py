#Write a program that receives a positive number greater than zero and calculates and displays:
#the number squared
#the number cubed
#the square root of the number
#the cube root of the number

import math

num = int(input("Positive number: "))

print(f"Number squared: {num*num}")
print(f"Number cubed: {num*num*num}")
print(f"Square root: {math.sqrt(num)}")
print(f"Cube root: {math.cbrt(num)}")
