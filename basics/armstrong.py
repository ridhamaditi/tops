num = int(input("Enter Number: "))

total = 0

while num > 0:
	r = num % 10
	total += r ** 3
	num //= 10

if total == num:
	print("Armstrong")
else:
	print("Not armstrong")