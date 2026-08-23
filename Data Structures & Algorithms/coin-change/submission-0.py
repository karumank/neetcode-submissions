class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        
        def dfs(amount_diff):
            if amount_diff == 0:
                return 0
            if amount_diff in cache:
                return cache[amount_diff]
            res = float("inf")
            for coin in coins:
                if amount_diff - coin >= 0:
                    res = min(res, 1 + dfs(amount_diff - coin))
            
            cache[amount_diff] = res
            
            return res
        
        minCoins = dfs(amount)
        
        return -1 if minCoins >= float("inf") else minCoins
            
            
            


