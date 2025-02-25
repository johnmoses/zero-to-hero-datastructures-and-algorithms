"""
Singly Linked List class with more functions
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, data=None):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(x.data) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        size = 0
        node = self.head
        while node: 
            size += 1
            node = node.next
        return size

    def add(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            self.tail = node
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        return self.tail

ll = LinkedList()
ll.add(10)
ll.add(20)
ll.add(30)

# Call special functions
print(ll)
print(len(ll))
