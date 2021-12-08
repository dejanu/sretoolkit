#!/usr/bin/env python3

# LIFO - push and pop
# =====
# |   |
# =====
# |   |
# =====
# |   |
# ===== 

class Stack():
    """ LIFO - push and pop"""

    def __init__ (self):
        self.items = []

    def isEmpty(self):
        """ return True if stack is empty """
        #return self.items == []
        return len(self.items) == 0

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        print("Pop last item aka first from the list")
        try:
            return self.items.pop(0)
        except IndexError:
            print("Stack is empty")
            return None

    def print_stack(self):
        print(self.items)

if __name__ == "__main__":

    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(5)
    s.print_stack()
    s.pop()
    s.pop()
    s.print_stack()
    s.pop()
    s.pop()
    s.pop()

