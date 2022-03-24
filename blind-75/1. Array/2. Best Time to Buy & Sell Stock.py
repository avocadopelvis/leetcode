# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Main idea: Buy low, sell high

# • set max profit to 0 and minimum price to infinity (we want the largest possible number to compare to, to get the minimum)
# • Iterate through the prices and update the min price  & max profit (profit = price - min price)
# • We get max profit if we subtract a price with the minimum price

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float('inf')
        
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
            
        return maxProfit
      
      
