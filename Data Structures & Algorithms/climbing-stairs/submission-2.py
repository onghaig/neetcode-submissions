class Solution:
    def climbStairs(self, n: int) -> int:
        currentStepways = 1
        previousStepWays = 1
        for i in range(n-1):
            temp = currentStepways
            currentStepways = previousStepWays + currentStepways
            previousStepWays = temp
        return currentStepways