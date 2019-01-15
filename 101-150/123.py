# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
#
# Example 1:
#
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#              Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# Example 2:
#
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


class Solution(object):
    # split to left and right part and find max profit, tle
    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     if not prices:
    #         return 0
    #     res = 0
    #     for i in range(len(prices)):
    #         res = max(res, self.maxProfitOne(prices[:i]) + self.maxProfitOne(prices[i:]))
    #     return res
    #
    # def maxProfitOne(self, prices):
    #     if not prices:
    #         return 0
    #     l, g = 2147483647, 0
    #     for price in prices:
    #         l = min(l, price)
    #         g = max(g, price - l)
    #     return g

    # better split dp
    # def maxProfit(self, prices):
    #     if not prices:
    #         return 0
    #     l, r = [0] * len(prices), [0] * len(prices)
    #     # left part when split at pos i
    #     local = prices[0]
    #     for i in range(len(prices)):
    #         local = min(local, prices[i])
    #         l[i] = max(l[i - 1], prices[i] - local)
    #     # right part when split at pos i
    #     # start at len-2 pos ( every transaction must have a start and end day.
    #     local = prices[-1]
    #     for i in range(len(prices) - 2, -1, -1):
    #         local = max(local, prices[i])
    #         r[i] = max(r[i + 1], local - prices[i])
    #
    #     g = 0
    #     for i in range(len(prices)):
    #         g = max(g, l[i] + r[i])
    #     return g


    # one pass dp
    def maxProfit(self, prices):
        buy1, sell1, buy2, sell2 = -float('inf'), 0, -float('inf'), 0
        for p in prices:
            sell2 = max(sell2, buy2 + p)
            buy2 = max(buy2, sell1 - p)
            sell1 = max(sell1, buy1 + p)
            buy1 = max(buy1, -p)
        return sell2


s = Solution()
print(s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
