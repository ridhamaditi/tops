# Aim: Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

try:
	l = input("Input values with space between them\n").split()
	for i in range(len(l)):
		l[i] = float(l[i])
	print("Maximum: ", max(l))
	print("Minimum: ", min(l))
except:
	print("Invalid input.")