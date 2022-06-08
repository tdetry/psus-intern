'''
Implement the method indexOf, which accepts a linked list (head) and a value, and returns the index (zero based) of the first occurrence of that value if exists, or -1 otherwise.

For example: Given the list: 1 -> 2 -> 3 -> 3, and the value 3, indexOf / index_of should return 2.

The linked list is defined as follows:

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

Note: the list may be null and can hold any type of value.

'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def index_of(head, value):
    if head is None: return -1
    index = -1

    while head is not None:
        if head.data == value:
            index += 1
            return index
        else: 
            index += 1
            head = head.next
    
    return -1


print(index_of(None, 17))# Expected: -1

n1 = Node(4)
n2 = Node(3, n1)
n3 = Node(2, n2)
head = Node(1, n3)
print(index_of(head, 2))# Expected: 1
    

n4 = Node('dfg')
n5 = Node('abc', n4)
n6 = Node('b', n5)
head_2 = Node('aaa', n6)
print(index_of(head_2, 'aaa'))# Expected: 0


