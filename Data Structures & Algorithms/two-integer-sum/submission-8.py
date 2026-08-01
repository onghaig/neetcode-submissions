class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            hashtable[nums[i]] = i
        for i,num in enumerate(nums):
            if (target - num) in hashtable and hashtable[target - num] != i:
                return [i,hashtable[target - num]]
        return []
        