import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # keep a min heap with size 2
        res = [] 
        for i,num in enumerate(nums):
            if res:
                peek = (res[0])
                if len(res) >= k and peek >= num:
                    continue
            heapq.heappush(res, num)
            if len(res) > k:
                heapq.heappop(res)
        return (res[0])