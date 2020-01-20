### histogram for letters ###


def create_histogram(l):
	""" l: list of str"""
	d = {}
	#create dict of letters 
	for word in l:
		for letter in word:
			if letter in d:
				d[letter]+=1
			else:
				d[letter]=1
	for i in d.keys():
		print("{}: {}".format(i, str("*"*d[i])))

if __name__ == "__main__":
	
	t = raw_input("Phrase: \n")
	create_histogram(t)
