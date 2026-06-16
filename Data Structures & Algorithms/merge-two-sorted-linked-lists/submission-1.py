# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        l1 = list1
        l2 = list2
        arr = []
        while l1:
            if l1 != None:
                arr.append(l1.val)
            l1 = l1.next
        while l2:
            if l2 != None:
                arr.append(l2.val)
            l2 = l2.next

        arr.sort()
        res = ListNode()
        curr = res
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next

        return res.next
            