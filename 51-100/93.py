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
        self.restore(s, [], res)
        return res

    def restore(self, s, path, res):
        if len(path) > 4:
            return
        if len(path) == 4:
            if s == '':
                res.append('.'.join(path))
            return
        for i in range(min(3, len(s))):
            if int(s[:i + 1]) <= 255:
                if i == 0 or s[0] != '0':
                    self.restore(s[i + 1:], path + [s[:i + 1]], res)


s = Solution()
print(s.restoreIpAddresses("0000"))
