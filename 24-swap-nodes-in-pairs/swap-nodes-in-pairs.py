# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        dummy_node.next = head

        cur = dummy_node
        

        while cur.next and cur.next.next:
            first = cur.next
            second = first.next
            afterPair = second.next

            cur.next=second
            second.next=first
            first.next = afterPair
            cur = first

        return dummy_node.next
        