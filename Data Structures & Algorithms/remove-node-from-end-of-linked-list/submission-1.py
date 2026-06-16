# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ret = head
        prev = None
        size = 0
        p = head
        while (p):
            size += 1
            p = p.next
        count = 1
        target = size - n
        if target == 0:
            return head.next
        while (head):
            if (count == target):
                head.next = head.next.next
                break
            prev = head
            head = head.next
            count += 1
        return ret