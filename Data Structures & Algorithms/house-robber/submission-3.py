class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        for i in range(len(nums)):
            rob1 = max(nums[i] + rob1, rob2)
            temp = rob2
            rob2 = rob1
            rob1 = temp
        return max(rob1,rob2)