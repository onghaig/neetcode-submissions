class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        res = []
        L = 0
        R = COLS - 1
        T = 0
        B = ROWS - 1
        while(L <= R and T <= B):
            for col in range(L, R + 1):
                res.append(matrix[T][col])
            T += 1
            for row in range(T,B + 1):
                res.append(matrix[row][R])
            R -= 1
            if(T <= B):
                for col in range(R, L-1, -1):
                    res.append(matrix[B][col])
                B -= 1
            if (L <= R):
                for row in range(B, T - 1, -1):
                    res.append(matrix[row][L])
                L += 1
        return res
