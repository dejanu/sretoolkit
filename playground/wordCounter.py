



def update_global_word_dict(w, d):
	"""count the letters in word w and update dict d"""
	for i in w.lower():
		if i in d:
			d[i]+=1
		else:
			d[i]=1
	return d


def text_list(text):
	""" text: string
	    return a list of words"""
	return text.split(" ")


def generate_stars(letter, counter):
	counter = int(counter)
	for i in range(counter):
		print(" \t Letter {} times: {} \t".format(letter,"*"*counter))


if __name__ == "__main__":
	
	global_dict = dict()

	t = "first text"
	tt = "a se"
	
	# split text in words and count letter in each word
	for word in text_list(t):
		global_dict = update_global_word_dict(word,global_dict)
	for word in text_list(tt):
		global_dict = update_global_word_dict(word,global_dict)
	
	print(global_dict)
	
	for k,v in global_dict.items():
		generate_stars(k,v)

	
