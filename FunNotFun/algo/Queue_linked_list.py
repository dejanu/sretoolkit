#!/usr/bin/env python

# https://www.hackerrank.com/challenges/30-linked-list
# https://www.hackerrank.com/challenges/30-linked-list-deletion/problem
# https://www.hackerrank.com/challenges/reverse-a-linked-list/

## Queue: FIFO - usage for buffers aka order operations
## Implementation using linked-list

## usual checks: head != None/NULL 
## access data: head.data
## go to next element: head.next
## insert in list: list_obj.insert(data)

class Node:
    """class for individual nodes"""
    def __init__ (self,data):
        self.data = data
        self.next = None #the pointer to the next element
    
    def __repr__(self):
        return self.data

    def get_data(self):
        """return the data from node"""
        return self.data

    def get_next(self):
        """return the next node"""
        return self.next

    def set_next(self,node):
        """link the node"""
        self.next = node

    def traverse(self):
        """ 
        start from head node and
        go until node data is None
        """
        #start from head
        node = self
        print(self.data)
        while node != None:
            print (node.data)
            node = node.next
            
class LinkedList:
    """ 
    the only info we need to store for a LinkedList
    is where the list starts: head
    """
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        # validate that the current node is not None
        while node is not None:
            yield node
            node = node.next
    
    def insert_first(self,node):
        """ 
        insert node at the begining of the list
        create a new node and point the list.head to it
        """
        node.next = self.head
        self.head = node

    def insert_end(self,node=None):
        """
        traverse the whole list and add the new node at the end
        """
        # create a new node if no node was passed
        if node is None:
            new_node = Node("default data")
        else:
            pass

        # check if it is the last node in the list
        if self.head == None:
            self.head = node
            node.next = None
        else:
            end = self.head
            while end.next != None:
                end = end.next

            # insert new node    
            end.next = node
            node.next = None
        
        return self.head

    def removeDuplicates(self,head):
        # if not head:
        #     return head
        # new_node = head
        # while new_node.next:
        #     if new_node.data == new_node.next.data:
        #         new_node.next = new_node.next.next
        #     else:
        #         new_node = new_node.next
        # return head
        d= {}
        while head:
            if head.data in d.keys():
                d[head.data]+=1
            else:
                d[head.data]=1
            head = head.next
        
        # create new queue
        self.head = None
        for i in d.keys():
            self.insert_end(Node(i))
        return self.head
        
    
    def reverseList(self,head):
        """ reverse list """
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current =  next
        self.head = prev
        return head

if __name__ == "__main__":

    llist =  LinkedList()
    print(llist)

    # create Node
    first_node = Node("a")
    llist.head = first_node
    print(llist)

    # create more Nodes
    second_node = Node("b")
    third_node = Node("c")
    first_node.next = second_node
    second_node.next = third_node
    print(llist)

    # insert Node at the end of the list
    llist.insert_end(node = Node("c"))
    llist.insert_end(node =  Node("b"))
    llist.insert_end(node = Node("Insert at the end"))

    # insert Node at the begining of the list
    llist.insert_first(node = Node("Insert at the begining"))
    print(llist)

    # reverse list
    llist.reverseList(llist.head)
    print(llist)

    # remove duplicates
    llist.insert_end(node = Node("Insert at the end"))
    print(llist)
    llist.removeDuplicates(llist.head)
    print(llist)