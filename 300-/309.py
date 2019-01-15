# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
#
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:
#
# Input: [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # see https://blog.csdn.net/zjuPeco/article/details/76468185
        if len(prices) <= 1:
            return 0
        s0,s1,s2=0,-prices[0],-float('inf')
        for p in prices:
            p0,p1,p2=s0,s1,s2
            s0 = max(p0,p2)
            s1 = max(p0-p,p1)
            s2 = p1+p
        return max(s0,s2)