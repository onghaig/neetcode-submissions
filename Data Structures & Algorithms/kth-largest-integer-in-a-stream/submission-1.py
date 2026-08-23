import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.maxHeap = [-x for x in nums]
        heapq.heapify(self.maxHeap)


    def add(self, val: int) -> int:
        heapq.heappush(self.maxHeap, -1 * val)
        localk = self.k
        heaptemp = self.maxHeap.copy()
        res = -1001
        while (localk > 0):
            res = heapq.heappop(heaptemp)
            localk -= 1
        return -1 * res
        # 3,3,3,2,1
        # k = 3
