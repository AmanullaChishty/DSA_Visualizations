class Node:
    def __init__(self,key,value):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy_head = Node(0,0)
        self.dummy_tail = Node(0,0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

        self.cache = {}
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = None
        node.next = None

    def insert_at_tail(self,node):
        last = self.dummy_tail.prev
        last.next = node
        node.prev = last
        node.next = self.dummy_tail
        self.dummy_tail.prev = node   

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.remove(node)
            self.insert_at_tail(node)
            return node.value

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert_at_tail(node)
        else:
            if len(self.cache) == self.capacity:
                node = self.dummy_head.next
                self.remove(node)
                del self.cache[node.key]
            new_node = Node(key,value)
            self.insert_at_tail(new_node)
            self.cache[key] = new_node
            
            
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)