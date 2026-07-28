class Solution:
    def rob(self, nums: List[int]) -> int:
        # how can we define this as a recursive solution? dont worry about dp for now
        total = 0
        memo = [-1] * len(nums)
        def dfs(i):
            if (i >= len(nums)):
                return 0
            if (memo[i] != -1):
                return memo[i]
            memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return memo[i]
        return dfs(0)