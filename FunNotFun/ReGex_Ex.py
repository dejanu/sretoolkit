import re

## . = any char besides new line
## * = 0 or more repetition of preceding RE
## + = 1 or more repetition of preceding RE
## ? = 0 or 1 repetition of preceding RE
## {m} = m copies of precedint RE e.g: a{5} matches aaaaa
## [a,z] = set of chars 

# split string with multiple delimiters
print(re.split('\W+', 'Hello,world;a:test')) #['Hello', 'world', 'a', 'test']

def remove_punctuation(s):
    """ Remove punctuation [?.!] from string s"""
    #exclusion in re is achieved [^a-z] == exclude letters
    return "".join(re.findall('[^!.,?]+',s))

# raw string = don't handle backslashes etc
print (r'\tRaw')
print('\t Raw with tab')

def get_name(s):
    """Return names from string s"""
    ## create re object
    pattern = re.compile("[A-Z][a-z]+")

    ## create iterator and print all matches
    matches = pattern.finditer(s)
    for i in matches:
        print(i)

###Return all word that start with uppercase
###Start with upper case letter follow by lower case letter: One or More times
#print(re.findall('[A-Z]+[a-z]+',phrase))


###Count how many words are in a phrase based on counting whitespaces
#print(len(re.findall(r'\s+',phrase))+1)

text_string='''Jesica aka Jas45ads is 15 years old, aJamia
and Daniel is 27 years old. Edowards is 97 and his mother 102 and some shitty 123uiyyy
FBHdsadk'''


#Return the ages
ages=re.findall(r'\d+',text_string)

if __name__ == "__main__":

    # remove punctuation from string
    print(remove_punctuation("This is, a string! But it has punctuation. How can we remove it???"))

    get_name(text_string)
