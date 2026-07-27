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

        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(row,col):
            distance = 0
            visited = set()
            visited.add((row,col))
            queue = deque()
            queue.append((row,col,0))
            while (queue):
                distance += 1
                curr  = queue.popleft()
                r,c,d = curr
                neighbors = [(r,c + 1), (r,c-1), (r+1, c), (r-1,c)]
                for nei in neighbors:
                    r1,c1 = nei
                    if not(r1 >= ROWS or r1 < 0 or c1 >= COLS or c1 < 0 or (r1,c1) in visited):
                        visited.add((r1,c1))
                        if (grid[r1][c1] == -1):
                            continue
                        queue.append((r1,c1,d+1))
                        if (grid[r1][c1] == 0):
                            return d+1
                            # return abs(row - r1) + abs(col - c1)
            return 2**31 - 1

        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] > 0):
                    # we have land that must be traversed
                    grid[r][c] = bfs(r,c)
        
        return
                




