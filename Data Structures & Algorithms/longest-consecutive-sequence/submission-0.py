class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestRun = 0
        table = set()
        for num in nums:
            table.add(num)
        # now we have a set

        for element in table:
            currRun = 0
            if (element - 1) not in table:
                j = element
                while(j in table):
                    currRun += 1
                    j += 1
                if currRun > longestRun:
                    longestRun = currRun

        return longestRun
        