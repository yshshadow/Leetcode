# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
#
# Example 1:
#
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:
#
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#              The third child gets 1 candy because it satisfies the above two conditions.

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # two array
        # l = len(ratings)
        # lr = [1] * l
        # rl = [1] * l
        # for i in range(1,l):
        #     if ratings[i] > ratings[i-1]:
        #         lr[i] = lr[i-1] + 1
        # for i in range(l-2,-1,-1):
        #     if ratings[i] > ratings[i+1]:
        #         rl[i] = rl[i+1] + 1
        # return sum([max(lr[i],rl[i]) for i in range(l)])

        # one array
        # l = len(ratings)
        # res = [1] * l
        # for i in range(1,l):
        #     if ratings[i] > ratings[i-1]:
        #         res[i] = res[i-1] + 1
        # for i in range(l-2,-1,-1):
        #     if ratings[i] > ratings[i+1]:
        #         res[i] = max(res[i],res[i+1] + 1)
        # return sum(res)

        # peak and vally
        if len(ratings) <= 1:
            return len(ratings)
        res = 0
        pre_slope = 0
        up, down = 0, 0

        def count(n):
            return (n * (n + 1)) / 2

        for i in range(1, len(ratings)):
            slope = 1 if ratings[i] > ratings[i - 1] else (-1 if ratings[i] < ratings[i - 1] else 0)
            if (pre_slope > 0 and slope == 0) or (pre_slope < 0 and slope >= 0):
                res += count(up) + count(down) + max(up, down)
                up, down = 0, 0
            if slope > 0:
                up += 1
            elif slope < 0:
                down += 1
            else:
                res += 1
            pre_slope = slope
        res += count(up) + count(down) + max(up, down) + 1
        return res


s = Solution()
s.candy([1, 2, 3, 4, 5, 3, 2, 1, 2, 6, 5, 4, 3, 3, 2, 1, 1, 3, 3, 3, 4, 2])
