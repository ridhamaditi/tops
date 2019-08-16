#Write a Python function to check whether a number is perfect or not.
def check(n):
    s=0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s == n :
    	print("perfect number")
    else:
    	print("not perfect number")
try:
	n=int(input("Enter number: "))
	check(n)
except:
	print("Error") 