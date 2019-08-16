# Aim: Write a Python program to read a file line by line store it into a variable.

f = open("test.txt", 'r')
fvar = []
fc = f.read().splitlines()
for i in fc:
	print(i)
	fvar.append(i)

print(f"List:\n\n{fvar}")
f.close()