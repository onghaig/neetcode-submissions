import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        while(len(maxHeap) > 1):
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if (x==y):
                continue
            if y > x:
                heapq.heappush(maxHeap, x-y)
                continue
        return -1 * maxHeap[0] if maxHeap else 0