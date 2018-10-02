# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
#
# Example:
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
# #

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 0 node is also a partition
        # for sequence, chose a number i as the root
        # the left sequence is the left subtree of root and the right is the right subtree
        # left from [1..i-1], right from [i+1,n] subtree number equal to [1..n-i]
        # for i, the number of BST is left sub * right sub

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1  # side with 0 node
        dp[1] = 1  # side with 1 node
        for i in range(2, n+1):
            for j in range(1, i+1):  # j is the chosen root number
                dp[i] += dp[j-1]*dp[i - j]
        return dp[n]

s=Solution()
print(s.numTrees(3))