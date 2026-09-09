class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # start from the edges:
        # have a dict[node: safe or unsafe]
        # do a dfs from every node of the edges
        # mark each O node as safe or unsafe
        # then iterate through the entire list changing any unsafe
        # to safe
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(r,c):
            if ((r,c) in visited or r >= ROWS or r < 0 or c>= COLS or c < 0 or board[r][c] == 'X'):
                return 
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or i == ROWS - 1 or j == 0 or j == COLS - 1:
                    dfs(i,j)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'
        