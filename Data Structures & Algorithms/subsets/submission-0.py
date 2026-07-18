class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # easy: include or exclude 
        # at each index, make a branch to decide whether we are including that element or not
        res = []
        curr = []
        def dfs(i):
            if (i >= len(nums)):
                res.append(curr.copy())
                return 
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            dfs(i+1)
        dfs(0)
        return res