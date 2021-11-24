class Node:
    
    def __init__ (self,val):
        self.val = val
        self.next = None #the pointer to the next element

    def get_data(self):
        """return the data from node"""
        return self.val

    def get_next(self):
        """return the next node"""
        return self.next

    def set_next(self,node):
        """link the node"""
        self.next = node

    def traverse(self):
        """ start from head node and
            go until node val is None"""
        #start from head
        node = self
        print(self.val)
        while node != None:
            print (node.val)
            node = node.next
            


#create node objects for the list
node0 = Node(12)
node1 = Node(99)
node2 = Node(37)


##node0.next = node1
node0.set_next(node1)
print(node0.next)
print(id(node1))
print(hex(id(node1)))

node0.traverse()


