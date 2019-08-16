try:
	f = open("temp1", 'r')
	l = f.read().split()
	ans = 0
	for i in l:
		ans += int(i)
	print("Sumation: ", ans)
	f.close()
except FileNotFoundError:
	print("No such file.")
except ValueError:
	print("Invalid data")
except:
	print("Unexcepted error.")
finally:
	print("File closed.")