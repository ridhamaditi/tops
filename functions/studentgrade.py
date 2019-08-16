def studentgrade(l):
	if type(l) != list :
		return "Error"
	avg=[]

	x=0
	y=0
	check=len(l[0])

	temp=1
	temp1=1
	s=0		

	while x!= len(l) :
		while y != len(l[x]) :
			if len(l[x])!=check :
				return "Error(No of arguments mismatch."
			if x==0 :
				if type(l[x][y]) != str :
					return "Error(Nested first list not contains all strings.)"
			else :
				if y==0 :
					if type(l[x][y]) != str : 
						return "Error(Nested list first element not string.)"
				else :
					if type(l[x][y]) != int :
						return "Error(Nested list elements not int.)"
			y+=1
		y = 0
		x += 1

    
	while temp!= len(l):
		while temp1 != len(l[temp]):
			s+=l[temp][temp1]
			temp1 += 1
		avg.append(s/(len(l[temp])-1))
		s=0
		temp1 = 1
		temp += 1
	return avg

print(studentgrade([['Student','Quiz 1','Quiz 2','Quiz 3'],['John',100,90,80],['McVay',88,89,99]]))