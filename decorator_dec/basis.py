import random


# decorator with arguments
def power_of(exponent):
    def powerr(f):
        def wrapp(*args):
            return f(*args) ** exponent
        return wrapp 
    return powerr

#classic decorator
def powerr(f):
    def wrapp(*args):
        return f(*args) ** 2
    return wrapp

#@powerr
@power_of(3)
def rand_no():
    #return random.choice([2,3,4])
    return 6



if __name__ == "__main__":

    print(rand_no())
