class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_head(self,data):
        new_node = Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data,end="-->")
            current = current.next
        print("None")

    def insert_at_tail(self,data):
        new_node = Node(data)

        current = self.head

        if current is None:
            self.head=new_node
            return
        
        while current.next:
            current = current.next
            
        current.next=new_node

    def search(self,value):
        current = self.head

        while current:
            if current.data==value:
                return True
            current = current.next
        return False
    
    def search_index(self,value):
        current = self.head
        count = 0

        while current:
            if current.data==value:
                return count
            current = current.next
            count +=1
        return -1

    def search_all_index(self,value):
        current = self.head
        count = 0
        indexes = []

        while current:
            if current.data==value:
                indexes.append(count)
            current = current.next
            count +=1
        return indexes

    def find_node(self, value):
        current = self.head

        while current:
            if current.data == value:
                return current

            current = current.next

        return None
        
    def find_nodes(self,value):
        current = self.head
        nodes = []

        while current:
            if current.data == value:
                nodes.append(current)
            current = current.next
        return nodes
        
    def delete_by_value(self,value):
        prev = None
        current = self.head

        while current:
            if current.data == value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next

                return True
            prev = current
            current = current.next
        return False
            