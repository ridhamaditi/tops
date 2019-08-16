#Write a Python program to access a function inside a function.
def innerfun():
	print("Entry inner function")
	print("Exit inner function")

def outerfun():
	print("Entry Outer function")
	innerfun()
	print("Exit Outer function")

outerfun()