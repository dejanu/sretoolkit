#python -m trace -t script.py

def m(x):
    """"
[(lambda x: x * 3), (lambda x: x * 3), ... (lambda x: x * 3)]
"""
    #return [lambda x:x*i for i in range(4)]
    l = list()
    for i in [0,1,2]:
        l.append(lambda x:x*i)
    return l





call_m = [mimi(2) for mimi in m("nu conteaza")]

