class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # use the largest first but 
        # depth first search
        # from 0 we can either add 1 , 5, 10 coins
        memo = {}
        def dfs(amount) -> int:
            nonlocal coins, memo
            if amount == 0:
                return 0 
            if amount in memo:
                return memo[amount]
            best = 1e9
            for i in range(len(coins)):
                new = amount - coins[i]
                if new < 0:
                    continue
                best = min(1 + dfs(new),best)
            memo[amount] = best
            return best
        minimum = dfs(amount)
        return -1 if minimum >= 1e9 else minimum
        # depth first search starting from some coin amount

        