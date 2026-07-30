from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        # stores indices
            # when sliding right, we will remove all indices less than the new one,
            # and we will remove all of the old indices
        # this way, q[0] will always have the maximum in the current window
        # [1] -> [2] -> [2,1] -> [2,1,0] -> 
        # sliding window:
        l = 0
        r =  k
        for i in range(k):
            while (q and nums[q[-1]] < nums[i]):
                q.pop()
            # while (q and q[0] <= l):
            #     q.popleft()
            q.append(i)
            # print(q)
        res.append(nums[q[0]])
        while (r < len(nums)):
            while (q and nums[q[-1]] < nums[r]):
                q.pop()
            while (q and q[0] <= r - k ):
                q.popleft()
            q.append(r)
            res.append(nums[q[0]])
            # print(q)
            l+= 1
            r += 1
        return res