class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr, total):
            # base cases:
            if (total == target):
                res.append(curr.copy())
                # we add and return
                return
            if(total > target):
            # if the total is grater than the target theres no possible way to get target (pos only)
                return
            if (i >= len(nums)):
                # if i is greater than the actual set of numbers, we will be adding nothing forever
                return 
            # choice by including or not including i
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            # remove that ith one (we added multiple)
            dfs(i+1, curr, total)
        dfs(0,[],0) 
        return res