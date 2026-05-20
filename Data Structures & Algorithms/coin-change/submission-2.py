class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(amount):
            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]

            res = 1e9
            for coin in coins:
                if amount - coin >= 0: # this means coin is valid
                    res = min(res, 1 + dp(amount - coin))
                # ow we do nothing
            memo[amount] = res # store this in cache
            return res
        
        minCoin = dp(amount)
        if minCoin >= 1e9:
            return -1
        return minCoin

        # coins.sort(reverse=True)
        
        # smallCoin = coins[len(coins) - 1]

        # i = 0
        # count = 0
        
        # while amount > smallCoin:
        #     while amount < coins[i]:
        #         i+=1
        #     amount -= coins[i]
        #     count +=1
            

        # if amount == 0:
        #     return count 
        # if amount % smallCoin == 0:
        #     return count+1
        # else:
        #     return  -1

