class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i,num in enumerate(nums):
            hmap[num] = i
        for i, num in enumerate(nums):
            goal = target - num
            if (goal in hmap and hmap[goal] != i):
                return [i, hmap[goal]]
        return [] 
