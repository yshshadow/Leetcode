# Given an absolute path for a file (Unix-style), simplify it.
#
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
#
# Corner Cases:
#
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".

class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # use O(n) space
        if not path or len(path) == 0:
            return ''
        paths = path.split('/')
        stack = []
        for p in paths:
            if p == '' or p == '.':
                continue
            elif p == '..':
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append('/' + p)
        if len(stack) == 0:
            return '/'
        else:
            return ''.join(stack)
        # use O(1) space
        # if not path:
        #     return ''
        # res = []
        # i = len(path) - 1
        # jump = 0
        # while i > -1:
        #     if path[i] == '/':
        #         i -= 1
        #     elif path[i] == '.':
        #         j = i
        #         while j > -1 and path[j] == '.':
        #             j -= 1
        #         if i - j == 2:
        #             i -= 2
        #             jump += 1
        #         elif i - j == 1:
        #             i -= 1
        #         else:
        #             if jump > 0:
        #                 jump -= 1
        #             else:
        #                 res.append(path[j + 1:i + 1])
        #             i = j - 1
        #     else:
        #         j = i
        #         while j > -1 and path[j] != '/':
        #             j -= 1
        #         if jump > 0:
        #             jump -= 1
        #         else:
        #             res.append(path[j + 1:i + 1])
        #         i = j - 1
        # return '/' + '/'.join(res[::-1]) if len(res) > 0 else '/'


s = Solution()
print(s.simplifyPath("/.../"))
print(s.simplifyPath("/a/./b/../../c/"))
