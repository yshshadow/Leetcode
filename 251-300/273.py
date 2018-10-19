# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
#
# Example 1:
#
# Input: 123
# Output: "One Hundred Twenty Three"
# Example 2:
#
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:
#
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# Example 4:
#
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"


class Solution(object):
    single = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    double = ['Zero', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    tenth = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
             'Nineteen']
    level = ['', 'Thousand', 'Million', 'Billion']

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        res = []
        level = 0
        while num > 0:
            num, mod = divmod(num, 1000)
            str = self.hunderdToWords(mod)
            if str != '':
                res.append(str + ' ' + self.level[level])
            level += 1
        return ' '.join(reversed(res)).rstrip()

    def hunderdToWords(self, num):
        if num == 0:
            return ''
        res = []
        if num >= 100:
            mod, num = divmod(num, 100)
            res.append(self.single[mod] + ' Hundred')
        if num >= 20:
            num, mod = divmod(num, 10)
            res.append(self.double[num] + (' ' + self.single[mod] if mod != 0 else ''))
        elif num >= 10:
            num, mod = divmod(num, 10)
            res.append(self.tenth[mod])
        elif num > 0:
            res.append(self.single[num])
        return ' '.join(res)


s = Solution()
print(s.numberToWords(1000010))
