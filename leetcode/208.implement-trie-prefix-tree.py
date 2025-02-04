#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start

class TrieNode:

    def __init__(self):
        self.array = [None]*26
        self.end_of_word = False

    def set_array_item(self, index, next_node):
        self.array[index] = next_node

    def get_array_item(self, index):
        return self.array[index]

    def set_end_of_word(self, value =True):
        self.end_of_word = value

    def get_end_of_word(self):
        return self.end_of_word
    
    
class Trie:

    '''
        Insert: O(word)
        Search: O(word)
        Check Prefix: O(prefix)

        Also made sure to access variables of other class using resp getters and setters
    '''

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for letter in word:
            index = ord(letter) - ord('a')
            
            if not curr.get_array_item(index):
                curr.set_array_item(index, TrieNode())
            curr = curr.get_array_item(index)
        curr.set_end_of_word()

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            index = ord(letter) - ord('a')

            if not curr.get_array_item(index):
                return False
            curr = curr.get_array_item(index)
        return curr.get_end_of_word()

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            index = ord(letter) - ord('a')

            if not curr.get_array_item(index):
                return False
            curr = curr.get_array_item(index)
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

