
# link: https://www.hackerrank.com/challenges/palindrome-index/problem

def palindromeIndex(s):
    # check if already palindrom
    if s==s[::-1]:
        return -1
    else:
        ls=list(s)
        # iterate thorugh half
        for i in range(len(ls)//2):
            if ls[i] != ls[-(i+1)]:
                new_list = s[:i] + s[i+1:]
                if(new_list == new_list[::-1]):
                    return i
                else:
                    return len(ls)-1-i