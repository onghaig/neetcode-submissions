# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:   
        # s, f pointers to split list
        s = head
        f = head.next
        while (s and f and f.next):
            s = s.next
            f = f.next.next
        
        # 123, 456
        # reverse second half
        second = s.next
        s.next = None
        prev = None

        while (second):
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # reverses 2nd half of list
        #  s will be at the end
        second = prev
        # 123 45
        p1 = head
        p2 = second
        while (p1 and p2):
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2
        return

        
            
        