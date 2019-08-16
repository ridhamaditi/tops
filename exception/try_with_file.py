try:
	f = open("type_of_errors.txt", "r")
	print(f.read())
	f.close()
except FileNotFoundError:
	print("No such file with that name.")
finally:
	print("file closed.")