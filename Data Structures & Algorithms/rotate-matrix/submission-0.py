class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        for row in range(ROWS // 2):
            temp = [0] * COLS
            for col in range(COLS):
                temp[col] = matrix[row][col] 
                matrix[row][col] = matrix[ROWS - row - 1][col]
                matrix[ROWS - row - 1][col] = temp[col]
        # we've flipped all the matrices
        # must take the transpose
        # print(matrix)
        print("hello")
        for row in range(ROWS):
            for col in range(row + 1, COLS):
                # if (row == col):
                #     continue
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp

        