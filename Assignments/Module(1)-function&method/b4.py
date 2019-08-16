#Write a Python function that checks whether a passed string is palindrome or not
def check(txt):
	if type(txt) != str :
		return "Error"
	a=[]
	for i in txt:
		if 65<=ord(i)<=90 or 97<=ord(i)<=122 or 48<=ord(i)<=57 :
			a.append(i)
		else:
			pass
	a1=''.join(a)
	t=a1.lower()
	t1=""
	for i in t:
		t1=i+t1
	if t==t1 :
		print("palindrome")
	else:
		print("not palindrome")
n=input("Enter string: ")
check(n)
