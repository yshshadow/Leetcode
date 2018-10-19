# Implement a magic directory with buildDict, and search methods.
#
# For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.
#
# For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.
#
# Example 1:
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
# Note:
# You may assume that all the inputs are consist of lowercase letters a-z.
# For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
# Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.

class Node(object):
    def __init__(self, word):
        self.word = word
        self.has_word = False
        self.node_list = {}


class MagicDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('')

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.insert(word)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word or len(word) == 0:
            return
        current = self.root
        for idx in range(len(word)):
            char = word[idx]
            if char not in current.node_list:
                current.node_list[char] = Node(char)
            if idx == len(word) - 1:
                current.node_list[char].has_word = True
            current = current.node_list[char]

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if not word or len(word) == 0:
            return False
        count = 0
        current = self.root
        return self.searchNode(word, 0, current, count)

    def searchNode(self, word, idx, cur, count):
        char = word[idx]
        # if char not in cur.node_list and idx != len(word) - 1:
        #     if count != 0:
        #         return False
        #     else:
        #         ans = False
        #         for node in cur.node_list.values():
        #             ans = ans or self.searchNode(word, idx + 1, node, count + 1)
        #         return ans
        # elif idx == len(word) - 1:
        #     if count == 0:
        #         return char not in cur.node_list and any([node.has_word for node in cur.node_list])
        #     else:
        #         return char in cur.node_list and cur.node_list[char].has_word
        # else:
        #     return self.searchNode(word, idx + 1, cur.node_list[word[idx]], count)
        if count != 0:
            if char not in cur.node_list and idx != len(word) - 1:
                return False
            elif idx == len(word) - 1:
                return char in cur.node_list and cur.node_list[char].has_word
            else:
                return self.searchNode(word, idx + 1, cur.node_list[word[idx]], count)
        else:
            if idx != len(word) - 1:
                ans = False
                for node in cur.node_list.values():
                    ans = ans or self.searchNode(word, idx + 1, node, count + 1 if node.word != char else count)
                return ans
            else:
                return any([node.word != char and node.has_word for node in cur.node_list.values()])


# Your MagicDictionary object will be instantiated and called as such:


obj = MagicDictionary()
obj.buildDict(["hello","hallo","leetcode","judge", "judgg"])
# print(obj.search('hello'))
# print(obj.search('hello'))
print(obj.search('judgg'))
# ["MagicDictionary", "buildDict", "search", "search", "search", "search", "search", "search"]
# [[], [["hello","hallo","leetcode","judge", "judgg"]], ["hello"], ["hallo"], ["hell"], ["leetcodd"], ["judge"], ["judgg"]]