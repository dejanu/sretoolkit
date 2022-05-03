
# We want to make a row of bricks that is goal inches long.
# We have a number of small bricks (1 inch each) and big bricks (5 inches each).
# Return True if it is possible to make the goal by choosing from the given bricks

def make_briks(small,big,goal):
    """
    small: no of small bricks with value 2
	big: no of small bricks with value  5
	"""
    #not enough  big briks
    if (goal > big*5 + small*2):
        return False
    #not enough small briks
    if small < goal%5:
        return False

    return True
        
