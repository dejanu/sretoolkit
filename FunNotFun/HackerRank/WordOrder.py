#link: https://www.hackerrank.com/challenges/word-order/problem

word_dict={}

for l in range(no_of_lines):
    line = input()
    if line in word_dict:
        word_dict[line]+=1
    else:
        word_dict[line]=1

# no of distinc words
print(len(word_dict.keys()))

# no of occurence for each word
print(" ".join(map(str,word_dict.values())))
