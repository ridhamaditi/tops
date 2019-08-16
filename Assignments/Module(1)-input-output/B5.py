# Aim: Write a Python program to read last n lines of a file.

def file_read_from_tail(fname, nlines):
        f = open(fname, 'r')
        fl = (f.read().splitlines())[::-1]
        for i in range(nlines):
        	print(fl[i])
        f.close()

file_read_from_tail('test.txt',2)