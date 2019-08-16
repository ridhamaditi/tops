import math

try:
	print("Enter x1, y1, x2, y2:\n")
	x1 = float(input())
	y1 = float(input())
	x2 = float(input())
	y2 = float(input())
	d = math.sqrt(math.pow((x2 - x1), 2) + (y2 - y1)**2)
	print("\nDistance: ", d)
except ValueError:
	print("Invalid Input.")
except:
	print("Error")