from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        empty = set()
        fresh = set()
        # find the rotten fruit
        # from each rotten fruit, perform dfs every minute
        # if 
        ROWS = len(grid)
        COLS = len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    rotten.add((row,col))
                if grid[row][col] == 1:
                    fresh.add((row,col))
                if grid[row][col] == 0:
                    empty.add((row,col))
        # bfs from each of the fresh nodes
        q = deque(rotten)
        level = 0
        while (q and len(fresh) > 0):
            for _ in range(len(q)):
                row,col = q.popleft()
                increments = [[1,0], [-1,0], [0,-1], [0,1]]
                for dr,dc in increments:
                    drow = row + dr
                    dcol = col + dc
                    if (drow,dcol) in fresh and drow < ROWS and dcol < COLS and drow >= 0 and dcol >= 0:
                        q.append((drow,dcol))
                        grid[drow][dcol] = 2
                        fresh.remove((drow,dcol))
            level += 1
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1
        return level


            # add up down left right
            # if its out of bounds, skip
            # if its empty, skip
            # find the nearest rotten. the maximum is the number of minutes
            # if any of the nodes is not near a rotten one, we must rope max
        
        