import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # should only store the top k elements in the heap
        topkElements = []
        for x,y in points:
            if topkElements:
                arr = topkElements[0][1]
                x1 = arr[0]
                y1 = arr[1]
                print(x1,y1)
                peekEuclidean = math.hypot(x1,y1)
            else:
                peekEuclidean = 999999
            currEuclidean = math.hypot(x,y)
            if len(topkElements) < k:
                heapq.heappush(topkElements,(-currEuclidean,[x,y]))
                print("topk < k")
                continue
            if peekEuclidean > currEuclidean:
                heapq.heappush(topkElements,(-currEuclidean,[x,y]))
                heapq.heappop(topkElements)
                print("peek > curr")
                print(peekEuclidean)
                print(currEuclidean)
                continue
            else:
                print("peek < curr")
                continue
        return [topkElements[i][1] for i in range(len(topkElements))]
        # need to remove the max element each time