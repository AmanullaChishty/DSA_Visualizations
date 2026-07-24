# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None:
            return head
        dummy_node = ListNode(0)
        dummy_node.next = head
        n = 0
        cur = dummy_node

        while cur.next:
            n+=1
            cur = cur.next

        tail = cur
        k = k%n

        if k == 0:
            return head
        node_before_cut = dummy_node

        for _ in range(n-k):
            node_before_cut = node_before_cut.next
        
        new_head = node_before_cut.next

        node_before_cut.next = None
        tail.next=dummy_node.next

        return new_head
        
        