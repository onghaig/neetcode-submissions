class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #  area is given by min of the heights, times the differences in their indices
        # how can we maximize this with two pointers?
        # p1 = 0 , p2 = end
        # 

        p1 = 0
        p2 = len(heights) - 1
        maxArea = 0
        while (p1 != p2):
            currArea = abs(p1 - p2) * (min(heights[p1],heights[p2]))
            if (currArea > maxArea):
                maxArea = currArea
            else:
                if (heights[p1] < heights[p2]):
                    p1 += 1
                else:
                    p2 -= 1
        return maxArea