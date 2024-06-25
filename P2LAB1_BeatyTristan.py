#Tristan Beaty
#6/25/2024
#P2LAB1
#Using the radius of a circle to calculate diameter, circumference, and area.

import math

print('What is the radius of the circle? ', end = ' ')
radius = float(input())
print()

diameter = 2 * radius
circumference = 2 * radius * math.pi
area = math.pi * radius**2

print(f'The diameter of the circle is {diameter:.1f}\n')

print(f'The circumference of the circle is {circumference:.2f}\n')

print(f'The area of the circle is {area:.3f}')


