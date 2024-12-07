class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        profit = 0

        for right in range(1, len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = max(profit, prices[right] - prices[left])    
        return profit
        
# T = O(n)
# S = O(1)