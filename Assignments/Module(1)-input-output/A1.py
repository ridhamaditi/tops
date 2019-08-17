#Write a Python program to read a random line from a file.
import random
def randomline(f):
    line = open(f).read().splitlines()
    return random.choice(line)
print(randomline('test.txt'))
