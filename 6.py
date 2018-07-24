# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".


class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or len(s) == 0 or numRows <= 0:
            return ""
        if numRows == 1:
            return s
        list = ""
        size = numRows * 2 - 2
        for i in range(numRows):
            for j in range(i, len(s), size):
                list += s[j]
                if i != 0 and i != numRows - 1 and j + size - 2 * i < len(s):
                    list += s[j + size - 2 * i]
        return list



