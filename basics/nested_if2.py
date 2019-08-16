pizza = int(input("Pizaz: "))
pasta = int(input("Pasta: "))

total = 0
free = ""

if pizza < 1 or pizza > 4:
	print("Pizza out of stock")
elif pizza == 1:
	total = total + 10
elif pizza == 2:
	total = total + 19
elif pizza == 3:
	total = total + 27
elif pizza == 4:
	total = total + 35
	free = free + "Free Coke "

if pasta < 1 or pasta > 4:
	print("Pasta out of stock")
elif pasta == 1:
	total = total + 10
elif pasta == 2:
	total = total + 19
elif pasta == 3:
	total = total + 27
elif pasta == 4:
	total = total + 35
	free = free + "Free Brownie "

print("\nTotal: ", total)
print(free)