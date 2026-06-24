# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next
        
        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node
        
        while prev:
            if head.val!=prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True
        