#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Time: O(n) ; Space: O(1)
        left = 0 #minimal
        right = 1

        maxProfit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right]- prices[left]
                maxProfit = max(profit, maxProfit)
            else:
                left=right
            right+=1

        return maxProfit
# @lc code=end

