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
    
    def delete_head(self):
        if self.head:
            self.head = self.head.next
    
    def delete_tail(self):
        prev=None
        current = self.head

        if current is None:
            return False
        
        if current.next is None:
            self.head = None
            return True

        while current:
            if current.next==None:
                prev.next = None
                return True
            prev = current
            current = current.next
    
    def insert_at_position(self,index, data):
        prev = None
        current = self.head
        count = 0
        new_node=Node(data)

        while current:
            if count == index:
                if prev is None:
                    new_node.next=self.head
                    self.head = new_node
                    return True
                else:
                    new_node.next=current
                    prev.next=new_node
                    return True
            count+=1
            prev=current
            current=current.next
        if count == index:
            if self.head:
                prev.next = new_node
            else:
                self.head = new_node
            return True
        return False
    
    def delete_at_index(self, index):
        prev = None
        current = self.head
        count = 0
        
        while current:
            if count == index:
                if prev is None:
                    self.head = current.next
                    return True
                else:
                    prev.next = current.next
                    return True
            count+=1
            prev = current
            current = current.next
        
        return False
    
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next #Save
            current.next = prev #Reverse
            prev = current #Advance
            current = next_node #Advance

        self.head = prev

        return True

    def merge_sorted_list(self,list1,list2):
        if not list2:
            return list1
        if not list1:
            return list2
        
        if list1.val<=list2.val:
            head = list1
            tail=list1
            list1 = list1.next
        else:
            head=list2
            tail=list2
            list2 = list2.next
            

        while list1 and list2:
            if list1.val<=list2.val:
                tail.next=list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next=list2
                tail = tail.next
                list2 = list2.next
        
        if not list2:
            tail.next=list1
        else:
            tail.next=list2

        return head 
        


            


        
            