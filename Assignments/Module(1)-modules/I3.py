# Aim: Write a Python program to calculate the area of a trapezoid.

try:
	height = float(input("Height of trapezoid: "))
	base_1 = float(input('Base one value: '))
	base_2 = float(input('Base two value: '))
	area = ((base_1 + base_2) / 2) * height
	print("Area is:", area)
except:
	print("Invalid input.")