class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {v: i for i,v in enumerate(nums)}
        for j,vj in enumerate(nums):
            if target - vj in hashtable:
                if hashtable[target-vj] == j:
                    continue
                return [j, hashtable[target-vj]]
        return []
