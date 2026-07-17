class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        complete = []
        def dfs(i, curr, total):
            if (total == target):
                complete.append(curr.copy())
                return 
            if (i >= len(nums) or total > target):
                return
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i + 1, curr, total)
        dfs(0, [], 0)
        return complete



#  2, 5, 6, 9
# we can choose to include 2, and each time recursively remove one thing

