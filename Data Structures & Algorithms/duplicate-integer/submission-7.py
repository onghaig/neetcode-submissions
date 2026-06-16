class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = set()
        for n in nums:
            if n in l:
                return True
            l.add(n)
        return False