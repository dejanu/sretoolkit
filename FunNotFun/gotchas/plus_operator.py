#!/usr/bin/env python3

## a+=b extends  and a = a + b creates new object

l = [i for i in range(10)]
ll = l

## create new object
ll+=[99999]

## extend original object
#ll = ll + [999999]


if __name__ == "__main__":

    print(f"l is {l} and ll is {ll}")
