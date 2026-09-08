class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {v: i for i,v in enumerate(nums)}
        for idx,val in enumerate(nums):
            goal = target - val
            if (goal in hashtable and hashtable[goal] != idx):
                return [idx,hashtable[goal]]
        return []