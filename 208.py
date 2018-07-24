# Implement a trie with insert, search, and startsWith methods.
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('')

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
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word or len(word) == 0:
            return False
        current = self.root
        for idx in range(len(word)):
            char = word[idx]
            if char not in current.node_list:
                return False
            elif idx == len(word) - 1 and not current.node_list[char].has_word:
                return False
            elif idx == len(word) - 1 and current.node_list[char].has_word:
                return True
            else:
                current = current.node_list[char]

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if not prefix or len(prefix) == 0:
            return False
        current = self.root
        for idx in range(len(prefix)):
            char = prefix[idx]
            if char not in current.node_list:
                return False
            elif idx == len(prefix) - 1:
                return True
            else:
                current = current.node_list[char]


class Node(object):
    def __init__(self, word):
        self.word = word
        self.has_word = False
        self.node_list = {}

        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)
