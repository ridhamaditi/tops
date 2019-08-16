n= int(input("Enter: "))

fact = 1

# while n > 1:
# 	fact = fact * n
# 	n -= 1

for i in range(1, n+1):
	fact = fact * i

print("Factorial: ", fact)