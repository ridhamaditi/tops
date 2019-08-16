#Write a Python function to calculate the factorial of a number (a non-negative integer)
def fac(n):
	fact=1
	for i in range(1,n+1):
		fact *= i
	print("Fact: ",fact)
try:
	n=int(input("Enter non-negative number: "))
	if n<0 :
		print("Error") 
	else:
		fac(n)	
except:
	print("Error")

