def isprime(n,i=2):
	if n <= 2:
		return True
	elif n % i == 0:
		return False
	elif i*i > n:
		return True
	else:
		return isprime(n,i+1)


n=int(input("Enter No: "))
j=isprime(n)
if j==True:
	print("Prime")
else:
	print("Not prime")