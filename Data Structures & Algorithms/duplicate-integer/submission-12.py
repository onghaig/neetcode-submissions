from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        if not count:
            return False
        return not max(count.values()) <= 1
        