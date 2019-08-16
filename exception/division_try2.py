a = (input("Enter a number:"))
b = (input("Enter a number:"))

try:
	a = int(a)
	b = int(b)
	c = a / b
	print(c)
except ZeroDivisionError:
	print("Can not divide by zero.")
except ValueError:
	print("Invalid input.")
except:
	print("Some error occured.")

print("This is an example of exception.")