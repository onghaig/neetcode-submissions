# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head #slow pointer
        p2 = head # fast pointer
        while (p2 and p2.next):
            if (p2 == None):
                return False
            p2 = p2.next.next
            p1 = p1.next
            if (p2 == p1):
                return True
        return False