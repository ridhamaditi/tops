# Aim: Write a Python program to read first n lines of a file.

def file_read_from_head(fname, nlines):
        f = open(fname, 'r')
        for i in range(nlines):
        	print(f.readline())
        f.close()

file_read_from_head('test.txt',2)