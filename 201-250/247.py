# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Find all strobogrammatic numbers that are of length = n.
#
# Example:
#
# Input:  n = 2
# Output: ["11","69","88","96"]

class Solution(object):
    rotate = {'0': '0', '1': '1', '6': '9', '9': '6', '8': '8'}

    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []
        if n == 1:
            return ["0", "1", "8"]
        length, remain = divmod(n, 2)
        res = []
        for start in ['1', '6', '9', '8']:
            self.search(length, 1, start, remain, res)
        return res

    def getPair(self, path):
        s = []
        for p in path[::-1]:
            s.append(self.rotate[p])
        return ''.join(s)

    def search(self, length, used, path, isodd, res):
        if length == used:
            if isodd:
                for mid in ["0", "1", "8"]:
                    res.append(path + mid + self.getPair(path))
            else:
                res.append(path + self.getPair(path))
        else:
            for c in self.rotate.keys():
                self.search(length, used + 1, path + c, isodd, res)

    # best solution
    # def findStrobogrammatic(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[str]
    #     """
    #     l = self.findS(n, {})
    #     if n > 1:
    #         l = [e for e in l if e[0] != '0']
    #     return l
    #
    # def findS(self, n, memo):
    #     if n in memo:
    #         return memo[n]
    #     d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    #     if n == 0:
    #         return []
    #     elif n == 1:
    #         return ['0', '1', '8']
    #     elif n == 2:
    #         return ["00", "11", "69", "88", "96"]
    #     else:
    #         base = self.findS(n - 2, memo)
    #     res = [k + e + d[k] for k in d for e in base]
    #     memo[n] = res
    #     return res