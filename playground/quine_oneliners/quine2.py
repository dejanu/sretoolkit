import inspect

def quine():
    source = inspect.getsource(quine)
    print(source)

quine()