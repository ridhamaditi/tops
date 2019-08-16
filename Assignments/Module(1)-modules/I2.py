# Aim: Write a Python program to convert degree to radian.

pi=22/7
try:
	degree = float(input("Input degrees: "))
	radian = degree*(pi/180)
	print(radian)
except:
	print("Invalid input.")