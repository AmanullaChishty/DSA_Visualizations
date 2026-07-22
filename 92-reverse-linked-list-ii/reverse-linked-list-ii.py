# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        dummy_node.next = head
        cur = dummy_node
        before = cur
        start = cur
        after = cur
        prev = None

        for _ in range(left-1):
            before = before.next
       
        start = before.next
        
        for _ in range(0,right+1):
            after = after.next
        
        cur = start
        
        while cur != after:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        before.next = prev
        start.next = after

        return dummy_node.next

        

            

        