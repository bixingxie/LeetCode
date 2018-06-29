class Solution(object):
    def maxProfit(self, prices):
        """
        time: O(n)
        space: O(1)
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0 
        lowest_price = float("inf")
        for price in prices: 
            lowest_price = min(lowest_price, price)
            profit = max(profit, price - lowest_price)
            #when price == lowest_price, it's zero, which is fine

        return profit
        
