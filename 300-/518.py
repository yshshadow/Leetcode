# You
# are
# given
# coins
# of
# different
# denominations and a
# total
# amount
# of
# money.Write
# a
# function
# to
# compute
# the
# number
# of
# combinations
# that
# make
# up
# that
# amount.You
# may
# assume
# that
# you
# have
# infinite
# number
# of
# each
# kind
# of
# coin.
#
# Note: You
# can
# assume
# that
#
# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the
# number
# of
# coins is less
# than
# 500
# the
# answer is guaranteed
# to
# fit
# into
# signed
# 32 - bit
# integer
#
# Example
# 1:
#
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there
# are
# four
# ways
# to
# make
# up
# the
# amount:
# 5 = 5
# 5 = 2 + 2 + 1
# 5 = 2 + 1 + 1 + 1
# 5 = 1 + 1 + 1 + 1 + 1
#
# Example
# 2:
#
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the
# amount
# of
# 3
# cannot
# be
# made
# up
# just
# with coins of 2.
#
# Example
# 3:
#
# Input: amount = 10, coins = [10]
# Output: 1

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0:
            return 1
        if not coins:
            return 0
        # 2d dp tle
        # dp = [[0 for _ in range(len(coins))] for _ in range(amount + 1)]
        # # for j in range(len(coins)):
        # #     if coins[j] <= amount:
        # #         dp[coins[j]][j] = 1
        # dp[0] = [1 for _ in range(len(coins))]
        # for i in range(1, amount + 1):
        #     for j in range(len(coins)):
        #         if coins[j] > i:
        #             dp[i][j] = dp[i][j - 1] if j > 0 else 0
        #         else:
        #             if j == 0:
        #                 dp[i][j] = dp[i-coins[j]][j] if i >= coins[j] else 0
        #             else:
        #                 for k in range(i // coins[j] + 1):
        #                     dp[i][j] += dp[i - k * coins[j]][j - 1]
        # return dp[-1][-1]
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i - coin]
        return dp[-1]


s = Solution()
s.change(5, [1, 2, 5])
