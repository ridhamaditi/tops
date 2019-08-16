# Aim: Write a python program to count the frequency of words in a file

def countWords(txt):
	if txt.isdigit():
		return "'error'"
	d = dict()
	words = txt.split()
	for word in words:
		d[word] = d.get(word, 0) + 1
	return d

txt = open("test.txt", "r").read()
Words = countWords(txt)
print("\n", Words)