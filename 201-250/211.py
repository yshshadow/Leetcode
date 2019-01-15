# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
#
# Example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = dict()


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        root = self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]
        root.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        root = self.root
        return self.dfs(root, word, 0)

    def dfs(self, node, word, index):
        if index == len(word) - 1:
            if word[index] != '.' and word[index] in node.children and node.children[word[index]].is_word:
                return True
            elif word[index] == '.' and any(node.children[child].is_word for child in node.children):
                return True
            else:
                return False
        else:
            if word[index] == '.':
                return any(self.dfs(node.children[child], word, index + 1) for child in node.children)
            elif word[index] in node.children:
                return self.dfs(node.children[word[index]], word, index + 1)
            else:
                return False


                # Your WordDictionary object will be instantiated and called as such:
                # obj = WordDictionary()
                # obj.addWord(word)
                # param_2 = obj.search(word)


s = WordDictionary()
s.addWord('bad')
s.addWord('dad')
s.addWord('mad')
print(s.search('pad'))
print(s.search('bad'))
print(s.search('.ad'))
print(s.search('b..'))
print(s.search('c..'))
print(s.search('...'))