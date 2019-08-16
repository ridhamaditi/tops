def joinedlist(n):
	l=[]
	if type(n)!= int:
		return "Error"
	if n > 0 :
		temp=0
		while temp<n :
			temp+=1
			l.append(temp)
		l.append(temp)	
		while temp>1 :
			temp-=1
			l.append(temp)		
	elif n < 0 :
		temp = n
		while temp < -1 :
			l.append(temp)
			temp+=1
		l.append(temp)
		temp=1
		while temp <= abs(n) :
			l.append(temp)
			temp+=1
	else:
		l.append(0)
	return l
l1=joinedlist(-5)
print(l1)