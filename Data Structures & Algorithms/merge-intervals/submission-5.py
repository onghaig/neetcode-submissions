class Solution:
    def merge(self, intervals : List[int][int]) -> List[int][int]:
        intervals.sort(key=lambda interval: (interval[0],interval[1]))
        merged = [intervals[0]]
        for start,end in intervals:
            if merged[-1][1] < start:
                merged.append([start,end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        return merged