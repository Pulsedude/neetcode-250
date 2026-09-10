from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_buy = prices[0]
        total_profit = 0
        n = len(prices)

        for i in range(1, n):
            if current_buy > prices[i]:
                current_buy = prices[i]
            
            if current_buy < prices[i]:
                total_profit += prices[i] - current_buy
                current_buy = prices[i]
        
        return total_profit

# Time: O(n)
# Auxiliary Space: O(1)

obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))