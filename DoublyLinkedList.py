class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
    

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self,val):
        new_node = Node(val)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size+=1
        
    def prepend(self, val):
        new_node = Node(val)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size+=1
        
    def remove_duplicates(self):
        cur = self.head
        
        while cur and cur.next:
            if cur.data == cur.next.data:
                cur.next = cur.next.next
            else:
                cur = cur.next
    
        
        
