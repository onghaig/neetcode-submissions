class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])
        def dfs(r, c, visit, height):
            if ((r,c) in visit or r < 0 or c < 0 or r >= rows or c >= cols):
                return 
            if (heights[r][c] < height):
                return
            visit.add((r,c))
            dfs(r,c + 1, visit, heights[r][c])
            dfs(r,c - 1, visit, heights[r][c])
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
        
        # left col, 
        for row in range(rows):
            dfs(row,0,pacific,heights[row][0])
        for col in range(cols):
            dfs(0,col,pacific,heights[0][col])
        
        for row in range(rows):
            dfs(row,cols-1,atlantic,heights[row][cols-1])
        for col in range(cols):
            dfs(rows-1,col,atlantic,heights[rows-1][col])
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append((r,c))
        return res