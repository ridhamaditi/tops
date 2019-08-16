try:
	f = open('temp2', 'w+')
	f.write("Hello")
	f.seek(0)
	print(f.read())
	f.close()
except:
	print("Error occured.")