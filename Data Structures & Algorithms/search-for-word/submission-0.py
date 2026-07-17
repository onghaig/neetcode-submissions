class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # board[][]
        ret = False
        for i,row in enumerate(board):
            for j,item in enumerate(row):
                if (item == word[0]):
                    # search the left and right
                    visited = set()
                    def dfs(r,c,k):
                        if (k == len(word)):
                            return True
                        if (r < 0  or r >= len(board) or c < 0 or c >= len(board[0]) or (r,c) in visited):
                            return False
                        if (board[r][c] != word[k]):
                            return False
                        visited.add((r,c))
                        found = dfs(r + 1, c, k + 1) or dfs(r, c + 1, k + 1) or dfs (r -1, c, k+ 1) or dfs (r, c-1, k+1)
                        visited.discard((r,c))
                        return found
                    if (dfs(i,j, 0) == True):
                        return True
                    else:
                        continue            
        return False
                        

                

