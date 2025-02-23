#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        '''
            Time:
             Let N be the number elements in board = n*m
                 K be the length of the word
            Think of this as a tree.. at each positin in the board it can branch out
              Now.. we will only branch to 3 places [we dont really extend the branch where we came from..]
              Those 3 branches can get to height of K at max

              So the tree would roughly have 3^K nodes [worst case]

            Therefore.. 
                time = #(nodes) * T(check_word_at_each_node)
                     =    3^K   *   N          
            O(N * 3^K)

            Space - 
                For mask O(N)
                For tree: We use dfs hence O(K)

                = O(N + K) = O(N) {N will aways be > K}
        '''
        #Next write the code using backtrack
        def check_word(i, j, word_pos, mask):
            if i < 0 or i >= len(mask) or j< 0 or j >= len(mask[0]):
                return False

            if mask[i][j]:
                return False
                  
            char = word[word_pos]
            if char != board[i][j]:
                return False
            mask[i][j] = 1   #set mask only when you include the element
            word_pos+=1
            if word_pos >= len(word):
                return True

            #right-down-left-up
            output = check_word(i, j+1, word_pos, mask) or check_word(i+1, j, word_pos, mask) or check_word(i, j-1, word_pos, mask) or check_word(i-1, j, word_pos, mask)     
            if output:
                return True
            mask[i][j] = 0
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                mask = [[0 for _ in row] for row in board]
                if check_word(i, j, 0, mask):
                    return True
        return False

# @lc code=end

