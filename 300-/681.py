# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.
#
# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
#
# Example 1:
#
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:
#
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.


class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        included = [int(x) for x in time if x != ':']
        cur = 60 * int(time[:2]) + int(time[3:])  # total minutes away from 00:00
        while True:
            cur = (cur + 1) % (24 * 60)  # add 1 min
            h, m = divmod(cur, 60)  # hour and minute
            a, b = divmod(h, 10)
            c, d = divmod(m, 10)
            if a in included and b in included and c in included and d in included:
                return '{}{}:{}{}'.format(a, b, c, d)

s=Solution()
print(s.nextClosestTime("23:59"))
