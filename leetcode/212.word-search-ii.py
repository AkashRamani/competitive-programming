#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.array = [None]*26
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for letter in word:
            index = ord(letter) - ord('a')

            if not curr.array[index]:
                curr.array[index] = TrieNode()
            curr = curr.array[index]
        curr.end_of_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()
        for word in words:
            trie.addWord(word)

        def check_word_in_board(i, j, curr_word, mask ,board, trie):
            if not trie:
                return

            if trie and trie.end_of_word:
                valid_words.add(curr_word)

            if i< 0 or i >=len(board) or j<0 or j>= len(board[0]) or mask[i][j]:
                return                    
    
            letter_index = ord(board[i][j]) - ord('a')
            if not trie.array[letter_index]:
                return

            mask[i][j] = 1
            curr_word = curr_word + board[i][j]
            trie = trie.array[letter_index]

            check_word_in_board(i, j+1, curr_word, mask, board, trie) #move-right
            check_word_in_board(i+1, j, curr_word, mask, board, trie) #move-down
            check_word_in_board(i, j-1, curr_word, mask, board, trie) #move-left
            check_word_in_board(i-1, j, curr_word, mask, board, trie) #move-up

            mask[i][j]= 0




        valid_words = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = trie.root
                mask = [[0 for _ in row] for row in board]
                # dfs
                check_word_in_board(i, j, "", mask ,board, curr)

        return list(valid_words)
        
# @lc code=end

