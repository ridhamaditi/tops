import math

print("Enter radius: ")
try:
	r = float(input())
	area = math.pi * math.pow(r, 2)
	volume = math.pi * (4.0/3.0) * math.pow(r, 3)
	print("\nArea:", area)
	print("\nVolume:", volume)
except ValueError:
	print("Invalid Input.")