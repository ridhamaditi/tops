#Write a Python program to remove newline characters from a file. 
def removenewlins(f):
    fl = open(f).readlines()
    return [s.rstrip('\n') for s in fl]

print(removenewline("test.txt"))