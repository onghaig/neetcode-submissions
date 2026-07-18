class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate through the matrix
        # if we find a 1, scan to mark the entire island as visited.
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0
        visited = set()
    
        for r in range(ROWS):
            for c in range(COLS):
               if grid[r][c] == "1" and (r,c) not in visited:
                    def dfs(r,c):
                        if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or grid[r][c] != "1"):
                            return 
                        visited.add((r,c))
                        dfs(r + 1, c)
                        dfs(r, c+1)
                        dfs(r-1, c)
                        dfs(r, c-1)
                        print("row: "+  str(r) + "column: "+ str(c) + "has been visited")
                        
                    dfs(r,c)
                    count += 1
                    print("count is: " + str(count))
        return count