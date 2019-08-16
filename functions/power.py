"""def power(m,n):
	i=1
	if ((type(m) != int) or (type(n)!=int)) :
		return "Error"
	else:
		while(True):
			if n**i==m :
				return i
			if n**i!=m and n**i>m:
				return -1
			else:
				i+=1

j = power(16,2)
print(j)"""


def power(m,n):
	count=0
	if ((type(m) != int) or (type(n)!=int)) :
		print("Error")
	while True :
		if (m%n == 0):
			count+=1
			m=m//n
			if(m==1):
				return count
		else:
			return -1

j = power(16,2)
print(j)






