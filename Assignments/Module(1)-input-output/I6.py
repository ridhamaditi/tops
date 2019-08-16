# Aim: Write a Python program to write a list content to a file.

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
f = open("test2.txt", "w")
for i in color:
	f.write(str(i))
f.close()
content = open('test2.txt')
print(content.read())
content.close()