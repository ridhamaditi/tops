def countWords(txt):
	if txt.isdigit():
		return "'error'"
	d = dict()
	words = txt.split()
	for word in words:
		d[word] = d.get(word, 0) + 1
	return d

txt = input("Enter string: ")
Words = countWords(txt)
print("\n", Words)