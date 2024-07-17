class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insert(self,head,data): 
    #Complete this method
        if head is None:
            head = Node(data)
            return head
        else:
            end = head
            while end.next:
                end=end.next
            end.next = Node(data)
            return head


def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node




prev = None
    current = llist
    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    llist = prev
    return llist