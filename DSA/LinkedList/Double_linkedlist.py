''' Double linked list - A linked list in which each node contains a reference (link) to the next node as well as to the previous node. 
This allows for traversal in both directions (forward and backward) through the list.
This is in contrast to a singly linked list, where each node only contains a reference to the next node, allowing for traversal in only one direction.
 '''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def add_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def print_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def print_backward(self):
        temp = self.tail
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

# Sample usage
dll = DoublyLinkedList()
dll.add_last(10)
dll.add_last(20)
dll.add_last(30)
dll.add_first(5)
dll.print_forward()    # Output: 5 <-> 10 <-> 20 <-> 30 <-> None
dll.print_backward()   # Output: 30 <-> 20 <-> 10 <-> 5 <-> None