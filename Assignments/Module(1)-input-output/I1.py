# Aim: Write a Python program to read a file line by line and store it into a list.

f = open("test.txt", 'r')
flist = []
fc = f.read().splitlines()
for i in fc:
	print(i)
	flist.append(i)

print(f"List:\n\n{flist}")
f.close()