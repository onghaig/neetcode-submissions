class Solution:
    def rob(self, nums: List[int]) -> int:
        def simpleRob(nums: List[int]) -> int:
            rob1, rob2 = 0, 0
            for i in range(len(nums)):
                temp = max(rob1 + nums[i], rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        run1 = simpleRob(nums[:len(nums) - 1])
        run2 = simpleRob(nums[1:])
        return max(run1,run2) if len(nums) > 1 else max(nums)