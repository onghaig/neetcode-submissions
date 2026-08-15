class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals by start, and then by end
        intervals.sort(key= lambda interval : (interval[0],interval[1]))
        # merge intervals by doing the following:
        merged = []
        for start,end in intervals:
            if len(merged) == 0 or merged[-1][1] < start:
                merged.append([start,end])
            else:
                merged[-1][1] = max(end,merged[-1][1])
        return merged
