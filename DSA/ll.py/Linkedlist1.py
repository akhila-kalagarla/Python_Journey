# class Node:
#     def __init__(self, data):
#         self.data = data 
#         self.next = None
# head = Node(1)
# tail = head 
# tail.next = Node(2)
# tail = tail.next
# tail.next = Node(3)
# tail = tail.next
# new_node = Node(4)
# new_node.next = head
# head = new_node
# print(head.data,tail.data,head.next.data,head.next.next.data)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.tail = None
        self.head = None
    def addlast(self,data):
        new_node = Node(data)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
    def add(self,data):
        new_node = Node(data)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def printdata(self):
        temp = self.head
        while temp!= None:
            print(temp.data,end="->")
            temp = temp.next
    
l1 = linkedlist()   
l1.addlast(10)
l1.addlast(20)
l1.addlast(30)
l1.add(40)
l1.printdata()


