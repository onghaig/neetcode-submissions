class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i,a in enumerate(nums):
            # i =index
            # a is nums[i]
            if (a > 0):
                break
            if (i>0) and nums[i-1] == a:
                continue
            l, r = i+1, len(nums) - 1
            while (l < r):
                currSum = nums[l] + nums[r] + a
                if (currSum > 0):
                    r-= 1
                    continue
                if (currSum < 0):
                    l +=1
                    continue
                if (currSum == 0):
                    temp = [a,nums[l],nums[r]]
                    ret.append(temp)
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ret

                
     
            

