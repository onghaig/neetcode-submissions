# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Node:
    def __init__(self, node):
        self.node = node
    def __lt__(self, node1):
        return self.node.val < node1.node.val
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # to track the next one to add, we will use a heap
        if len(lists) == 0:
            return None
        res = ListNode(0)
        cur = res
        heapoflists = []
        for l in lists:
            if (l is not None):
                heapq.heappush(heapoflists,Node(l))

        while heapoflists:
            removed = heapq.heappop(heapoflists)
            cur.next = removed.node
            cur = cur.next
            if (removed.node.next):
                heapq.heappush(heapoflists, Node(removed.node.next))
        return res.next
        
        