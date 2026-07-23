# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        dummy_node.next = head
        cur = dummy_node
        before = cur
        start = cur.next

        while True:
            after = before
            for _ in range(k):
                if after.next:
                    after = after.next
                else:
                    return dummy_node.next

            prev = after.next

            count = 1
            group_head = start

            while count <=k:
                next_node = start.next
                start.next = prev

                prev = start
                start = next_node

                count+=1

            before.next = prev
            before = group_head
        
        


        