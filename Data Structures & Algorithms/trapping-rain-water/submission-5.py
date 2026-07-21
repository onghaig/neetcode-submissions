class Solution:
    def trap(self, height: List[int]) -> int:
        # height = min(h1,h2) * (h2i - h1i)
        total = 0

        for i,h in enumerate(height):
            maxleftheight = height[i]
            maxrightheight = height[i]
            for l in range(i,-1, -1):
                maxleftheight = max(maxleftheight,height[l])
            for r in range(i + 1, len(height)):
                maxrightheight = max(maxrightheight,height[r])
            print("maxleftheight is: " + str(maxleftheight) +  " maxrightheight is: " + str(maxrightheight) + " index is " + str(i))
            volume = min(maxleftheight, maxrightheight) - height[i]
            print("volume is: " + str(volume))
            total += max(volume,0)
        return total
             