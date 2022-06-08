'''
Implement the method length, which accepts a linked list (head), and returns the length of the list.

For example: Given the list: 1 -> 2 -> 3 -> 4, length should return 4.

The linked list is defined as follows:

class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

Note: the list may be null and can hold any type of value.
'''

class Node:
    def __init__(self, data: int, next = None):
        self.data = data
        self.next = next


def length(head): 
    length = 0
    if head == None:
        return length

    while head != None:
        length += 1
        head = head.next
    
    return length


print(length(None)) #Expected: 0


n1 = Node(1)
n2 = Node(2, n1)
n3 = Node(3, n2)
head = Node(4, n3)

print(length(head)) # Expected: 4