# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Psuedo Code:
# traverse both 

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur1 = headA
        cur2 = headB
        lenA=0
        lenB=0

        while cur1:
            lenA+=1
            cur1 = cur1.next
        while cur2:
            lenB+=1
            cur2 = cur2.next

        cur1 = headA
        cur2 = headB

        if lenA>lenB:
            for _ in range(lenA-lenB):
                cur1 = cur1.next
        elif lenB > lenA:
            for _ in range(lenB-lenA):
                cur2 = cur2.next
        
        
        while cur1 and cur2:
            if cur1 == cur2:
                return cur1
            cur1 = cur1.next
            cur2 = cur2.next
        return None
        