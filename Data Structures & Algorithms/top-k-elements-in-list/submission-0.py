from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        numCount = Counter(nums)
        for i in range(k):
            res[i] = numCount.most_common(k)[i][0]
        return res