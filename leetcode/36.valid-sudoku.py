#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Solution1 : For each value at i,j => comparing with 3 hash maps {each for row, col, block}

        '''defaultdict(set): doesnot give No key error, essentially comparable to doing.. in a dictionary
        hash_col = {for i in ra }
        for key, val in range(0, n):
            hash_col[key] = {}
            
        Linear Pass: Time Complexity O(n^2) // or Linear in the size of input
        Memory : O(n^2)
        '''
        n=len(board)

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(n):
            for col in range(n):
                element = board[row][col]
                if element == ".":
                    continue
                is_element_in_row = element in rows[row]
                is_element_in_col = element in cols[col]
                is_element_in_block = element in squares[(row//3, col//3)] #since tuple is immutable and can be used as a key
                if (is_element_in_row or is_element_in_col or is_element_in_block):
                    return False

                cols[col].add(element)
                rows[row].add(element)
                squares[(row//3, col//3)].add(element)
        return True
        
# @lc code=end

