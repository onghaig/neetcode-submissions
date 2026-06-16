# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        head1 = head
        while list1 and list2:
            if list1.val > list2.val:
                head.next = list2
                list2 = list2.next
                print(head.next.val) 
            else:
                head.next = list1
                list1 = list1.next
                print(head.next.val)  
            # else:
            #     head.next = list1
            #     head.next.next = list2
            #     list1 = list1.next
            #     list2 = list2.next
            #     # print(head.next.val)  
            head = head.next
        head.next = list1 or list2
        return head1.next