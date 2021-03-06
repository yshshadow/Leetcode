# In
# an
# alien
# language, surprisingly
# they
# also
# use
# english
# lowercase
# letters, but
# possibly in a
# different
# order.The
# order
# of
# the
# alphabet is some
# permutation
# of
# lowercase
# letters.
#
# Given
# a
# sequence
# of
# words
# written in the
# alien
# language, and the
# order
# of
# the
# alphabet,
# return true if and only if the
# given
# words
# are
# sorted
# lexicographicaly in this
# alien
# language.
#
# Example
# 1:
#
# Input: words = ["hello", "leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As
# 'h'
# comes
# before
# 'l' in this
# language, then
# the
# sequence is sorted.
# Example
# 2:
#
# Input: words = ["word", "world", "row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As
# 'd'
# comes
# after
# 'l' in this
# language, then
# words[0] > words[1], hence
# the
# sequence is unsorted.
# Example
# 3:
#
# Input: words = ["apple", "app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The
# first
# three
# characters
# "app"
# match, and the
# second
# string is shorter( in size.) According
# to
# lexicographical
# rules
# "apple" > "app", because
# 'l' > '∅', where
# '∅' is defined as the
# blank
# character
# which is less
# than
# any
# other
# character(More
# info).
#
# Note:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All
# characters in words[i] and order
# are
# english
# lowercase
# letters.
import itertools


class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        orderdict = {c: i for i, c in enumerate(order)}
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                def compare(w1, w2):
                    for c1, c2 in itertools.zip_longest(w1, w2, fillvalue=order[0]):
                        if orderdict[c1] < orderdict[c2]:
                            return True
                        elif orderdict[c1] > orderdict[c2]:
                            return False
                    return True

                if not compare(words[i], words[j]):
                    return False
        return True


s = Solution()
print(s.isAlienSorted(["hello", "leetcode"],
                      "hlabcdefgijkmnopqrstuvwxyz"))
