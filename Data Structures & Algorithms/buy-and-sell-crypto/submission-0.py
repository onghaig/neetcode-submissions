class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxp = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                currprof = prices[r] - prices[l]
                maxp = max(currprof,maxp)
                r += 1
            else:
                l = r
                r+=1
        return maxp