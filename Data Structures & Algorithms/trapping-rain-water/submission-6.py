class Solution:
    def trap(self, height: List[int]) -> int:
        #  we know that we can determine the amount of water at each position
        #  using this formula:
        #  volume = min(height[l],heigh[r]) - height[i],
        # where height[l] is the leftmost tallest, and height[r] is the right most tallest
        # 
        # left subarray
        res = 0
        l = 0
        r = len(height) - 1
        maxleft = height[l]
        maxright = height[r]
        while (l < r):
            if (maxleft < maxright):
                res += max(maxleft - height[l],0)
                l+=1
                maxleft = max(maxleft,height[l])
            else:
                res += max(maxright - height[r], 0)
                r -= 1
                maxright = max(maxright,height[r])

        return res

            
