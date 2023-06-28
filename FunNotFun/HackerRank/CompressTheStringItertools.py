
# link: https://www.hackerrank.com/challenges/compress-the-string/problem

# count consecutive occurences

s= list(map(int,input()))
counter=0
new=[]
prev=None

for i in s:
    if prev!=None:
        if i==prev:
            # visited the elem 
            counter+=1
        elif i!=prev:
            new.append((counter,prev))
            prev=i
            counter=1    
    else:
        #element not visited
        prev=i
        counter+=1
        
new.append((counter,prev))     
print(*new)  
