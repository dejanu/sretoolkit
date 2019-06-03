## Check anagram for two string e.g dog == God
## or "public relations" anagram of "crap built on lies"


def check_anagram(s,ss):
    """check if we have same letters 
        and the same no. of letters in both strings"""
    s = s.replace(" ","").lower()
    ss = ss.replace(" ","").lower()
    return sorted(ss) == sorted(s)

def check_anagram_dict(s,ss):
    #check the no of letters in the 2 strings
    if len(s)!=len(ss):
        return False
    else:
        #dict for s
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        #dict for ss
        for j in ss:
            if j in d:
                d[j]-=1
            else:
                d[j]=1
        #the values of the dict should be zero at the end
    return d.values()
            
##generate alphabet
import string
alphabet = string.ascii_lowercase

if __name__ == "__main__":
    print(check_anagram("God ","dog"))
    print(check_anagram("public Relations","crap built on lies"))
    print(check_anagram_dict("publicrelations","crapbuiltonlies"))
    
    #create string from list 
    s1 = ''.join(str(i) for i in range(1,10))
    print(s1)
    from string import ascii_lowercase
    print(ascii_lowercase)
