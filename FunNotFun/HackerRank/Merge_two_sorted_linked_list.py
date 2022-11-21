
# link: https://www.hackerrank.com/challenges/one-week-preparation-kit-merge-two-sorted-linked-lists/problem


def quick_sort(s):
    """quick sort"""
    if len(s)<=1:
        return s
    else:
        p=s[0]
        ls = [ i for i in s[1:] if i<=p]
        lg = [ i for i in s[1:] if i>p]
    return quick_sort(ls)+[p]+quick_sort(lg)

def mergeLists(head1, head2):
    """ 
    1,3,7
    1,3
    result: 1,1,2,3,7 
    """
    merged_list = []
    # create obj of type SinglyLinkedList
    merged_list_typed = SinglyLinkedList()
    
    while (head1 != None):
        merged_list.append(head1.data)
        head1 = head1.next
    
    while (head2 != None):
        merged_list.append(head2.data)
        head2 = head2.next
        
    # sort the regular list    
    sorted_merged_list=quick_sort(merged_list)
    
    # insert nodes
    for i in sorted_merged_list:
        merged_list_typed.insert_node(i)