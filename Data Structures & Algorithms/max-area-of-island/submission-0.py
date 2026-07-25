class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # scan through the matrix
        #  if we hit a 1, we perform dfs throughout the connected regions to catch all
        # local land
                #  after finding the island, we add each (x,y) to a hashmap indexed by location
                #  and the location is tied to some area
                # this will serve as our visited.
        # we also keep a running maximum of the total area
        ROWS, COLS = len(grid), len(grid[0])
        visited = {}
        currIsland = 0
        maxSize = 0
        for row in range(ROWS):
            for col in range(COLS):
                status = grid[row][col]
                if status == 1 and (row,col) not in visited:
                    currSize = 0
                    def dfs(row,col):
                        if (row >= ROWS or row < 0 or
                                col >= COLS or col < 0 or
                                (row,col) in visited or
                                grid[row][col] == 0):
                                return 0 
                        visited[(row,col)] = currIsland
                        return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
                    currSize = dfs(row,col)
                    maxSize = max(currSize, maxSize)
                    currIsland += 1
                if status == 0:
                    visited[(row,col)] = 0
        print(visited.items())
        return maxSize
