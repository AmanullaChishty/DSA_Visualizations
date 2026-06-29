"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        
        cur = head

        while cur:
            new_node = Node(cur.val)
            next_original = cur.next

            cur.next = new_node

            new_node.next = next_original

            cur = cur.next.next

        cur = head

        while cur:
            copy = cur.next
            if cur.random:
                copy.random = cur.random.next
            cur = cur.next.next
        
        cur = head
        copy_head = head.next

        while cur:
            copy = cur.next
            cur.next = cur.next.next

            if copy.next:
                copy.next = copy.next.next
            cur = cur.next
        return copy_head



        
        
            
        
        


        