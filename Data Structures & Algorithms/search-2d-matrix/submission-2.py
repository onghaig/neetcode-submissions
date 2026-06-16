class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search through rows; get 1st and last of each row, compare it. if bigger than least and less than most, we have the right row
        m = len(matrix)
        n = len(matrix[0])
        firstinRow = 0
        lastinRow = n - 1
        start = 0
        end = m - 1
        ourRow = -1
        if (target < matrix[0][firstinRow]):
            return False
        if (target > matrix[end][lastinRow]):
            return False            
        while (start <= end):
            mid = (start + end) // 2
            if (matrix[mid][firstinRow] <= target and matrix[mid][lastinRow] >= target):
                ourRow = mid
                break
            elif (matrix[mid][lastinRow] < target):
                start = mid + 1
            elif (matrix[mid][lastinRow] > target):
                end = mid - 1
        print(ourRow)
        #ourRow is working
        start = 0
        end = n-1         
        while (start <= end):
            mid = (start + end) // 2
            if (matrix[ourRow][mid] < target):
                start = mid + 1
            elif (matrix[ourRow][mid] > target):
                end = mid - 1
            else:
                return True
        return False
