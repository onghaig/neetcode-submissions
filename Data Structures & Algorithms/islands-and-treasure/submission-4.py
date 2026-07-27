from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # m x n 2d grid, with 3 possible values for each
        # -1 water cell cannot be traversed
        #  0 a treasure chest
        # inf - land cell that can be traversed

        # we want to fill each land cell with the distance to its nearest treasure chest
        # this is going to be breadth-first-search
        # the distance is given by the total number of steps
        queue = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == 0):
                    queue.append((r,c, 0))
        dist = 0                     
        while (queue):
            curr = queue.popleft()
            r,c, d = curr
            neighbors = [(r,c+1, d+1), (r,c-1, d+1), (r+1,c, d+1), (r-1,c, d+1)]
            for nei in neighbors:
                r,c,d = nei
                if (r >= ROWS or r < 0  or c >= COLS or c < 0 or grid[r][c] != 2147483647):
                    continue
                grid[r][c] = d
                queue.append((r,c, d))

        
        return
                

