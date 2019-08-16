#Write a program in Python to reverse a string without using inbuilt function reverse string?
s=input("Enter string: ")
rev=""
for i in s:
	rev=i+rev
print("reversed string: ",rev)