class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        for row in range(ROWS):
            seen = set()
            for col in range(COLS):
                if(board[row][col] == "."):
                    continue
                if (board[row][col] in seen):
                    return False
                seen.add(board[row][col])
        for col in range(COLS):
            seen = set()
            for row in range(ROWS):
                if(board[row][col] == "."):
                    continue
                if (board[row][col] in seen):
                    return False
                seen.add(board[row][col])
        # 3x3 
        print("test")
        for x in range(0,9,3):
            for y in range(0,9,3):
                print("x is" + str(x) + "y is" + str(y))
                seen = set()
                for r in range(x,x+3):
                    for c in range(y,y+3):
                        if board[r][c] == ".": continue
                        if board[r][c] in seen:
                            return False
                        seen.add(board[r][c])

        return True
