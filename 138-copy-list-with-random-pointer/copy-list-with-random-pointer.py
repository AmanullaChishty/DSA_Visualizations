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
        mapping ={}
        if head is None:
            return None

        copy_head = Node(head.val)

        copy_curr = copy_head
        cur = head.next
        mapping[head]=copy_head

        while cur:
            new_node = Node(cur.val)
            copy_curr.next = new_node

            mapping[cur]=new_node

            copy_curr = copy_curr.next
            cur = cur.next

        cur = head
        
        while cur:
            copy = mapping[cur]
            copy.random = mapping.get(cur.random)
            cur = cur.next
            
        return copy_head
        