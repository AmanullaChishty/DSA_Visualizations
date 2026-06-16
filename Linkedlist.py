class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #stores refernce to next node

# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)

# n1.next = n2
# n2.next = n3

# print(n1.data)
# print(n1.next.data)
# print(n1.next.next.data)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head

        while current.next:
            current = current.next
        
        current.next = new_node

    def print_list(self):
        current = self.head

        while current:
            print(current.data,  end=" -> ")
            current = current.next
        print('None')
    
    def length(self):
        current = self.head
        count = 0
        while current:
            count+=1
            current = current.next
        return count
    
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
       


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()
ll.length()