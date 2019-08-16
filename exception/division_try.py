a = int(input("Enter a number:"))
b = int(input("Enter a number:"))

try:
	c = a / b
	print(c)
except:
	print("Can not divide by zero.")

print("This is an example of exception.")