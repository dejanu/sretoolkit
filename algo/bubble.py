#!/usr/bin/python

def bubble_one(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i]<l[j]:
                l[i],l[j]=l[j],l[i]
    return l


def bubble_two(l):
    """the real shhit"""
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j]<l[j+1]:
                 l[i],l[j+1]=l[j+1],l[i]
    return l


if __name__ == "__main__":
    l=[55,2,9,0,42,123]
    print(bubble_two(l))
    print(bubble_one(l))
