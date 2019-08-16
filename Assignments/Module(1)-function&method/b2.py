 #Write a Python function to check whether a number is in a given range
def check(n,n1,n2):
	if n>=n1 and n<=n2 :
		print("Number in range.")
	else :
		print("Number not in range.")
try:
	n1=int(input("Enter lower limit: "))
	n2=int(input("Enter upper limit: "))
	n=int(input("Enter number: "))
	check(n,n1,n2)
except:
	print("Error") 