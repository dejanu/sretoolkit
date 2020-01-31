#Journey through the CPython Interpreter
# https://dbader.org/blog/python-mystery-dict-expression


d = {True: "yes", 1: "no", 1.0: "maybe"}

# the output is {True: "maybe"}
print(d)

# the interpreter creates a new dict and assigns the k,v in the order give by the dict expression

# d = dict()
# d[True] = 'yes'
# d[1] = 'no'
# d[1.0] = 'maybe'

# keys are evaluated as equal behind scenes
# because bool is a subtype/subclass of int => bool var can be use as indexes 
print(True == 1 == 1.0)

