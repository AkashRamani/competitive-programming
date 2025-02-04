#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.dict = {}
        self.end_of_word = False

    def get_node(self, letter):
        return self.dict.get(letter)
    
    def update_node(self, letter, next_node):
        self.dict[letter] = next_node

    def set_end_of_word(self, value):
        self.end_of_word = value

    def get_end_of_word(self):
        return self.end_of_word
    def get_dict(self):
        return self.dict

class WordDictionary:
    '''
        Inseart: O(N), N = len of word

        Search: O(26^L) where L is the number of '.' (wildcards)... 
                    example: for word => `ab..c.` ==> {1 * 1 * 26 * 26 * 1 * 26}  ~ O(26^3)
                best case for search (zero wild cards): O(N) N is the length of the word
    '''

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if not curr.get_node(letter):
                curr.update_node(letter, TrieNode())
            curr = curr.get_node(letter)
        curr.set_end_of_word(True)
            
    # dfs
    def search(self, word: str, node = None) -> bool:
        curr = node
        if not curr:
            curr = self.root

        for i, letter in enumerate(word):
            if letter == '.':
                for alp ,node in curr.get_dict().items():
                    if self.search(word[i+1:], node):
                        return True
                return False

            if not curr.get_node(letter):
                return False
            curr = curr.get_node(letter)
        return curr.get_end_of_word()


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

