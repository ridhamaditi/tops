# Aim: Write a Python program to copy the contents of a file to another file.

f1 = open("test.txt")
v = f1.read()
f1.close()
f2 = open("test2.txt", "w")
f2.write(v)
f2.close()