class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = {None}
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False
            