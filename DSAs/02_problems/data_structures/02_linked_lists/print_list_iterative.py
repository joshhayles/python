# Write a function, print_list, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None

# create instances of the Node class, with their corresponding values and assign them to variables:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

# establish a link between the nodes using the "next" attribute:
a.next = b
b.next = c
c.next = d

def print_list(head):
    current = head 

    while current is not None:
        print(current.val)
        current = current.next

print_list(a)