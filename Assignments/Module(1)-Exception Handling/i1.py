#write program for Catching Specific Exceptions in Python
a=input("Enter 1st number: ")
b=input("Enter 2nd number: ")
try:
	a=int(a)
	b=int(b)
	c=a/b
	print(c)
except(ZeroDivisionError):
	print("Zero division error.")
except(ValueError):
	print("Value error.")
except:
	print("Unexpected error")
