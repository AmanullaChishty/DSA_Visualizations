# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Psuedo Code:
# n should go to 2 position
# n-1 should go to 
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
      
        second = slow.next
        slow.next = None

        prev = None
        curr = second

        while curr:
            next_node = curr.next
            curr.next= prev

            prev = curr
            curr = next_node
        
        first = head
        second = prev
        while second:
            tmp1 = first.next  #Save the pointers
            tmp2 = second.next #Save the pointers

            first.next = second #merging
            second.next = tmp1  #reconnecting the remainder of first

            first = tmp1 #advance
            second = tmp2 #advance



            


        