# A
# chess
# knight
# can
# move as indicated in the
# chess
# diagram
# below:
#
# .
#
# This
# time, we
# place
# our
# chess
# knight
# on
# any
# numbered
# key
# of
# a
# phone
# pad(indicated
# above), and the
# knight
# makes
# N - 1
# hops.Each
# hop
# must
# be
# from one key
#
# to
# another
# numbered
# key.
#
# Each
# time
# it
# lands
# on
# a
# key(including
# the
# initial
# placement
# of
# the
# knight), it
# presses
# the
# number
# of
# that
# key, pressing
# N
# digits
# total.
#
# How
# many
# distinct
# numbers
# can
# you
# dial in this
# manner?
#
# Since
# the
# answer
# may
# be
# large, output
# the
# answer
# modulo
# 10 ^ 9 + 7.
#
# Example
# 1:
#
# Input: 1
# Output: 10
# Example
# 2:
#
# Input: 2
# Output: 20
# Example
# 3:
#
# Input: 3
# Output: 46
#
# Note:
#
# 1 <= N <= 5000

class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        paths = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [1, 6], 8: [1, 3],
                 9: [2, 4]}
        dp = [[0 for _ in range(10)] for _ in range(N)]
        for i in range(10):
            dp[0][i] = 1  # no jump
        for i in range(1, N):
            for j in range(10):
                for k in paths[j]:
                    dp[i][j] += dp[i - 1][k]
        return sum(dp[N - 1]) % (10 ** 9 + 7)


s = Solution()
print(s.knightDialer(4))
