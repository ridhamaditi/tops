# Aim: Write a python program to count the number of lines in a text file.

f = open("test.txt", 'r')
fc = f.read().splitlines()
print("Lines:", len(fc))
f.close()