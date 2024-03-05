# Write a function, print_list, that takes in the head of a linked list as an argument and prints all the values of the nodes in the linked list, but with using recursion.

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
    # establish base case 
    if head is None:
        return
    
    print(head.val)
    print_list(head.next)


print_list(a)