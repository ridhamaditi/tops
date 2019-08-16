def check(dic,txt):
	final=''
	flag =0
	t1=txt.split()
	for i in t1:
		for j in dic:
			if i==j :
				final = final + dic[j]
				final += " "
				flag =1
		if (flag==0)	:	
			final = final + i
			final += " " 
		flag =0 

	return final


dic={'up':'down','down':'up'}
txt='up down up down forward'
f=check(dic,txt)
print(f)
