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
            copy = Node(cur.val)
            next_node = cur.next
            cur.next = copy
            copy.next = next_node
            cur = next_node
        
        cur = head

        while cur:
            copy= cur.next

            if cur.random:
                copy.random = cur.random.next
            cur = cur.next.next
        
        cur = head
        copy_head = head.next
        copy = copy_head

        while cur:
            cur.next = copy.next
            if copy.next:
                copy.next = copy.next.next

            cur = cur.next
            copy = copy.next
        
        return copy_head
        