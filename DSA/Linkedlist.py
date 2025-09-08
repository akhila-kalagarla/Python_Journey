# class Node:
#     def __init__(self, value = 0, next_node = None):
#         self.data = value
#         self.next = next_node 
# p1 = Node(10,None)
# p2 = Node(20)
# p3 = Node()
# print(p1.data)
# print(p2.data)6
# print(p3.data)

class Node:
    def __init__(self, data):   # Corrected __init__
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):        # Corrected __init__
        self.head = None

    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new 

    def insert_pos(self, pos, data):
        new = Node(data)
        if pos == 0:   # Insert at head
            new.next = self.head
            self.head = new
            return  

        temp = self.head
        for i in range(pos-1):
            if temp is None:   # Invalid position
                print("Position out of range")
                return
            temp = temp.next 

        if temp is None:
            print("Position out of range")
            return

        new.next = temp.next
        temp.next = new

    def display(self):
        temp = self.head 
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next 
        print("None")

# Example usage
l1 = LinkedList()
l1.insert_begin(30)
l1.insert_begin(80)
l1.insert_pos(1, 50)   # Insert at position 1
l1.insert_pos(0, 100)  # Insert at beginning
l1.insert_pos(3, 60)   # Insert at position 3
l1.display()

### Deletion in Linked List ###

# Deletion at begining
def delete_begin(self):
    if not self.head:
        print("List is empty")
        return
    self.head = self.head.next

# Deletion at end
def delete_begin(self):
    if not self.head:
        print("List is empty")
        return
    if not self.head.next:
        self.head = None
        return
    temp = self.head
    while temp.next.next:
        temp = temp.next
    temp.next = None
    
# Deletion at position
def delete_pos(self, pos):
    if not self.head:
        print("List is empty")
        return
    if pos == 0:
        self.head = self.head.next
        return
    temp = self.head
    for i in range(pos-1):
        if not temp.next:
            print("Position out of range")
            return
        temp = temp.next
    if not temp.next:
        print("Position out of range")
        return
    temp.next = temp.next.next


