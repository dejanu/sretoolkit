# python stack data structure implementation LIFO

# =====
# |   |
# =====
# |   |
# =====
# |   |
# ===== 



class Stack():
    """ Python 3.x implementation"""

    def __init__ (selfi):
        self.items = list()

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        # default behaviour for pop is list.pop(-1)
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return "".join(self.items)
