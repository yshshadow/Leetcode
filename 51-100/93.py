# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# Example:
#
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.restore(s,0,'',res)
        return res

    def restore(self, s, level, pre, res):
        if len(pre) == len(s) + 4:
            res.append(pre)
            return
        
