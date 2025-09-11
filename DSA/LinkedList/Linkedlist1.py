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
    def findatindex(self,index):
        temp = self.head   
        i = 0
        while i < index:
            temp = temp.next
            i+=1
        return temp 
    def insert(self,index,data):
        if index == 0:
            self.add(data)
            return
        new_node = Node(data)
        prev = self.findatindex(index-1)
        new_node.next = prev.next
        prev.next = new_node
        if new_node.next == None:
            self.tail = new_node
    def deletelast(self):
        temp = self.head
        while temp.next!=self.tail:
            temp = temp.next
        temp.next = None
        self.tail = temp
    def deletefirst(self):
        self.head = self.head.next
    def deleteatindex(self, index):
        temp = self.findatindex(index-1)
        temp.next = temp.next.next
    def searchnode(self, key):
        temp = self.head
        while temp != None:
            if temp.data == key:
                return True 
            else:
                temp = temp.next
            return False


l1 = linkedlist()   
l1.addlast(10)
l1.addlast(20)
l1.addlast(30)
l1.addlast(40)
l1.addlast(50)
l1.addlast(60)
l1.printdata()

l1.deletefirst()
print()
l1.printdata()
l1.deletelast()
print()
l1.printdata()
l1.deleteatindex(1)
print()
l1.printdata()

