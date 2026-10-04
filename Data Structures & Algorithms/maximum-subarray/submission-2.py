class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-11000] * len(nums) 
        dp[0] = nums[0]  
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        best = -11001
        for num in dp:
            best = max(best, num)
        return best