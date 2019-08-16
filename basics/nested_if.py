age = int(input("Enter Age: "))
weight = int(input("Enter weight: "))

if age >= 18:
	if weight > 50:
		print("eligible")
	else:
		print("not eligible")
else:
	print("not eligible")