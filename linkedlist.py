class Node:
     def __init__(self, value = None,next = None,prev =None):
         self.prev = prev
         self.value = value
         self.next = next


class LinkedList:
    def __init__(self):
        self.head = None 



n1 = Node(2)
n2 = Node(3)
n3 = Node(4)
n4 = Node(5)

LL = LinkedList()
LL.head = n1

n1.next = n2
n2.next = n3
n3.next = n4

print(n1.value)


