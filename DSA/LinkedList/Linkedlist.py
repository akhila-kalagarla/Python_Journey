# Linked list 
class Node:
    def __init__(self, value = 0, next_node = None ):
        self.data = value
        self.next = next_node 
p1 = Node(10,None )
p2 = Node(20)
p3 = Node()
print(p1.data)
print(p2.data)
print(p3.data)

class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None  

class LinkedList:
    def __init__(self):        
        self.head = None 

    # Insert at beginning
    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new 

    # Insert at given position
    def insert_pos(self, pos, data):
        new = Node(data)
        if pos == 0:   # Insert at head
            new.next = self.head
            self.head = new
            return  

        temp = self.head
        for i in range(pos - 1):
            if temp is None:   # Invalid position
                print("Position out of range")
                return
            temp = temp.next 

        if temp is None:
            print("Position out of range")
            return
        new.next = temp.next
        temp.next = new

    # Update node at position
    def update(self, pos, new_data):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        for i in range(pos):
            if not temp:
                print("Position out of range")
                return
            temp = temp.next
        if temp:
            temp.data = new_data

    # Delete at beginning
    def delete_begin(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next

    # Delete at end
    def delete_end(self):
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

    # Delete at given position
    def delete_pos(self, pos):
        if not self.head:
            print("List is empty")
            return
        if pos == 0:
            self.head = self.head.next
            return
        temp = self.head
        for i in range(pos - 1):
            if not temp.next:
                print("Position out of range")
                return
            temp = temp.next
        if not temp.next:
            print("Position out of range")
            return
        temp.next = temp.next.next

    # Display list

    def display(self):
        temp = self.head 
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next 
        print("None")

    # Traverse (same as display but with message)
    def traverse(self):
        if not self.head:
            print("List is empty")
            return
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
print("Initial List:")
l1.display()

print("\nAfter update at position 2:")
l1.update(2, 99)
l1.display()

print("\nAfter deleting at beginning:")
l1.delete_begin()
l1.display()

print("\nAfter deleting at end:")
l1.delete_end()
l1.display()

print("\nAfter deleting at position 1:")
l1.delete_pos(1)
l1.display()

### Double linked list ### 
#INSERTION AND DELETION AT BEGINNING, END AND GIVEN POSITION
class DNode:
    def __init__(self):
        self.head = None
    
    # Insertion at beginning
    def insert_begin(self, data):
        new = Node(data)
        if not self.head:
            self.head = new 
            return
        new.next = self.head
        self.head.prev = new
        self.head = new
    
    # Insertion at end
    def insert_end(self, data):
        new = Node(data)
        if not self.head:
            self.head = new 
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new 
        new.prev = temp

    # Insertion at given position
    def insert_pos(self, pos, data):
        new = Node(data)
        if pos == 0:
            self.insert_begin(data)
            return
        temp = self.head
        for i in range(pos - 1):
            if not temp:
                print("Position out of range")
                return
            temp = temp.next
        if not temp:
            print("Position out of range")
            return
        new.next = temp.next
        new.prev = temp
        if temp.next:
            temp.next.prev = new
        temp.next = new
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
D = DNode()
D.insert_begin(10)
D.insert_begin(20)
D.insert_end(30)
D.insert_pos(1, 25)
D.insert_pos(0, 5)
D.display()


# DELETION AT BEGINNING, END AND GIVEN POSITION
class DNode:
    def __init__(self):
        self.head = None

    # Insertion at beginning
    def insert_begin(self, data):
        new = Node(data)
        if not self.head:
            self.head = new 
            return
        new.next = self.head
        self.head.prev = new
        self.head = new
    
    # Insertion at end
    def insert_end(self, data):
        new = Node(data)
        if not self.head:
            self.head = new 
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new 
        new.prev = temp

    # Insertion at given position
    def insert_pos(self, pos, data):
        new = Node(data)
        if pos == 0:
            self.insert_begin(data)
            return
        temp = self.head
        for i in range(pos - 1):
            if not temp:
                print("Position out of range")
                return
            temp = temp.next
        if not temp:
            print("Position out of range")
            return
        new.next = temp.next
        new.prev = temp
        if temp.next:
            temp.next.prev = new
        temp.next = new

    # Deletion at beginning
    def delete_begin(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    # Deletion at end
    def delete_end(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    # Deletion at given position
    def delete_pos(self, pos):
        if not self.head:
            print("List is empty")
            return
        if pos == 0:
            self.delete_begin()
            return
        temp = self.head
        for i in range(pos):
            if not temp:
                print("Position out of range")
                return
            temp = temp.next
        if not temp:
            print("Position out of range")
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next
        temp = None # Free memory
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

