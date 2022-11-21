
# link: https://www.hackerrank.com/challenges/one-week-preparation-kit-new-year-chaos


def minimumBribes(q):
    # NewYearChaos(q)
    # q the list with persons after bribing [1,2,3,5,4,6,7,8]
    bribes=0
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2),i):
            if q[j] > q[i]:
                bribes+=1
    print(bribes)