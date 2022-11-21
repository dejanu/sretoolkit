
#link: https://www.hackerrank.com/challenges/one-week-preparation-kit-queue-using-two-stacks/problem

queue=[]
def queue_stack(operation,elem=None):
    # 1: enqueue 2: dequeue 3:print the front element
    if operation==1:
        queue.append(elem)
    elif operation==2:
        queue.pop(0)
    elif operation==3:
        print(queue[0])

no_q=int(input())
for _ in range(no_q):
    op = list(map(int,input().split()))
    if len(op)>1:
        operation=op[0]
        elem=op[1]
        queue_stack(operation,elem)
    else:
        operation=op[0]
        queue_stack(operation)
