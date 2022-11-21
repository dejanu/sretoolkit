
def isBalanced(s):
    o = ["(","[","{"]
    c = [")","]","}"]
    stack =[]
    for i in s:
        if i in o:
            stack.append(i)
        elif i in c:
            index_i = c.index(i)
            # check if the last element from the stack was an open param
            if (len(stack)>0 and o[index_i]==stack[-1]):
                stack.pop()
            else:
                return "NO"
    if len(stack)>0:
        return "NO"
    else:
        return "YES"