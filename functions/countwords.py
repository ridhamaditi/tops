def countwords(a):
	if type(a) != str :
		return "Error"
	s=[]
	for i in a:
		if 65<=ord(i)<=90 or 97<=ord(i)<=122 :
			s.append(i)
		elif i=="'" :
			s.append(i)
		else:
			s.append(" ")
	a1=''.join(s)
	a=a1.split()
	l=[i.lower() for i in a]
	temp=0
	b=[]
	for i in l:
		for j in l:
			if i==j:
				temp+=1
		b.append(temp)
		temp=0
	d=dict(zip(a,b))
	return d

article="He will be the president of the company; right now he's a vice president. But he himself, is no sure of it...(Later he will see the importance of these 3.)"
print(countwords(article))