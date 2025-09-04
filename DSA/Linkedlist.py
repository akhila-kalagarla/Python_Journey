class Node:
    def __init__(self, value = 0, next_node = None):
        self.data = value
        self.next = next_node 
p1 = Node(10,None)
p2 = Node(20)
p3 = Node()
print(p1.data)
print(p2.data)
print(p3.data)