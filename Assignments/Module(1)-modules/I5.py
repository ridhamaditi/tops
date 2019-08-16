# Aim: Write a Python program to calculate surface volume and area of a cylinder.

pi=22/7
try:
	height = float(input('Height of cylinder: '))
	radian = float(input('Radius of cylinder: '))
	volume = pi * radian * radian * height
	sur_area = ((2*pi*radian) * height) + ((pi*radian**2)*2)
	print("Volume is: ", volume)
	print("Surface Area is: ", sur_area)
except:
	print("Invalid input.")