class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l, r, mid pointer
        l = 0
        r = len(nums) -1

        while l < r:
            m = l + ((r - l) //2)
            if (nums[m] > nums[r]):
                l = m + 1
                continue
            if (nums[m] < nums[r]):
                r = m

        return nums[l]
