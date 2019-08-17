#write program that will ask the user to enter a number until they guess a stored number correctly
a=10
try:
	n=int(input("Enter number: "))
	while a!=n :
		print("Enter again")
		n=int(input("Enter number: "))
	print("Yay")
except:
	print("Error")
	

