import random

#generate board
board = [i for i in range(0,9)]


def showBoard():
    print("\n")
    print board[0]," | ",board[1]," | ",board[2]
    print "----------------"
    print board[3]," | ",board[4]," | ",board[5]
    print "----------------"
    print board[6]," | ",board[7]," | ",board[8]
    print "----------------"
    print("\n")

def getWinner(xoro):
    """verify if we have a line of x or 0"""

    if board[0]==xoro and board[1]==xoro and board[2]==xoro:
        return True
    elif board[3]==xoro and board[4]==xoro and board[5]==xoro:
        return True
    elif board[6]==xoro and board[7]==xoro and board[8]==xoro:
        return True
    elif board[2]==xoro and board[4]==xoro and board[6]==xoro:
        return True
    elif board[0]==xoro and board[4]==xoro and board[8]==xoro:
        return True
    elif board[0]==xoro and board[3]==xoro and board[6]==xoro:
        return True
    elif board[1]==xoro and board[4]==xoro and board[7]==xoro:
        return True
    elif board[2]==xoro and board[5]==xoro and board[8]==xoro:
        return True
    else:
        return False

def computerRespone():
    """generate random pc choice"""
    pc_input = random.choice(range(0,9))
    bol = True
    while bol == True:
        if board[pc_input] != "x" and board[pc_input] != "o":
            board[pc_input]="o"
            bol = False
        else:
           pc_input = random.choice(range(0,9))
                                            
            
while True:
    user_input=raw_input("Select a place on the board \n")
    user_input = int(user_input)

    if board[user_input] != "x" and board[user_input] != "o":
        board[user_input] = "x"
        showBoard()
    else:
        print("this spot is taken")
    computerRespone()
    showBoard()
    if getWinner("x") == True:
        print("X is the winner")
        break

    elif getWinner("o") == True:
        print("O is the winner")
        break
