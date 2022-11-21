
# link: https://www.hackerrank.com/challenges/piling-up/problem
# problem: There is a horizontal row of N cubes. The lenght of each cube is given. You need to create a new vertical pile of cubes.

# ANS = []
# T = int(input())

# for _ in range(T):
#     n = int(input())
#     sl = list(map(int, input().split()))

#     for _ in range(n-1):
#         if sl[0] >= sl[-1]:
#             a = sl.pop(0)
#         else:
#             # sl[0] < sl[-1]:
#             a = sl.pop(-1)
            
#         if len(sl) == 1:
#             ANS.append("Yes")

#         if((sl[0] > a) or (sl[-1] > a)):
#             ANS.append("No")
#             break

# print("\n".join(ANS))

def pile(size,blocks):
    """ 
    size: len(blocks)
    blocks: list with elements
    """
    for _ in range(size-1):
        if blocks[0] >= blocks[-1]:
            a = blocks.pop(0)
        else:
            # sl[0] < sl[-1]:
            a = blocks.pop(-1)            
        if len(blocks) == 1:
            return "Yes"
        if((blocks[0] > a) or (blocks[-1] > a)):
            return ("No")  

test_cases=int(input())
for i in range(test_cases):
    size=int(input())
    # convert string '3,4,2,4' into list of ints
    blocks=list(map(int,input().split()))
    print(pile(size,blocks))