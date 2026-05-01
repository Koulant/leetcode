class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        result = 0

        while r < len(prices): 
            # Price to buy at
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                result = max(result, profit)
            # Advance left if no profit
            else:
                l = r
            # Advance right always to scan to the right of buy price
            r += 1

        return result 



       
            


