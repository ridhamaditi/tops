# Aim: Write a Python program to find the sum of the following decimal numbers and display the numbers in sorted order.

l = input("Input values with space between them\n").split()
	for i in range(len(l)):
		l[i] = float(l[i])
print("Sum: ", sum(l))
print("Sorted order: ", sorted(l))