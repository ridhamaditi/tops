def palindrome(txt):
	if type(txt) != str :
		return "Error"
	a=[]
	for i in txt:
		if 65<=ord(i)<=90 or 97<=ord(i)<=122 :
			a.append(i)
		else:
			pass
	a1=''.join(a)
	t=a1.lower()
	
	#t1=''.join(reversed(t))
	t1=""
	for i in t:
		t1=i+t1

	if t==t1 :
		return True
	else:
		return False

print(palindrome("Cigar?!! Toss it in a can.! It is so tragic.!"))