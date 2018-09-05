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
                stack.append(p)
        if len(stack) == 0:
            return '/'
        else:
            return '/'.join(stack)

s=Solution()
print(s.simplifyPath("/home/"))
print(s.simplifyPath("/a/./b/../../c/"))
