class Solution:
    def maxProfit(self, prices):
        """
        time: O(n)
        space: O(1)
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0 
        for i in range(len(prices) - 1): 
            if prices[i + 1] > prices[i]: 
                profit = profit + prices[i + 1] - prices[i]
        return profit
