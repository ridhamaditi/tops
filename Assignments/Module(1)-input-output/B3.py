# Aim: Python program to append text to a file and display the text.

def file_read(fname):
        f = open(fname, 'a')
        f.write("\nPython Programs")
        f.close()
        txt = open(fname)
        print(txt.read())
file_read('test.txt')