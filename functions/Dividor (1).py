def check(m,n):
	k=[]
	if type(n) != int or type(m) != list:
		return "Error"
	for i in m:
		#print(type(i))
		if(type(i) == int or type(i) == float):
			k.append(i/n)
	return k

j=check([2,4,'a',4.5],2)
print(j)