#creating node class for creating nodes
class Node:
    def __init__(self , value = None , next = None):
        self.value = value
        self.next = next

#creating a linkedList class
class LinkedList:
    def  __init__(self):
        self.head = None

#initialising the LinkedList class
LL = LinkedList()

#creating nodes 
n1 = Node(2)
n2 = Node(5)
n3 = Node(8)
n4 = Node(15)
n5 = Node(20)

#creating a linkedList

#initiliasing the head

LL.head = n1

#next value of node 1
n1.next = n2
n2.next = n3
n3.next = n4