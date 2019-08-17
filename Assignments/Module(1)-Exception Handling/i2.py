#write python program for file operations to makes sure the file is closed even if an exception occurs.
f=open('temp.txt','r')
try:
	print(f.read())
except:
	print("Error")
finally:
	f.close()
	