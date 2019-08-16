def removepunctuation(n):
	if type(n) != str:
		return "Error"
	s=[]
	for i in n:
		if 65<=ord(i)<=90 or 97<=ord(i)<=122 :
			s.append(i)
		else:
			s.append(" ")
	return ''.join(s)
print(removepunctuation("A//..az"))