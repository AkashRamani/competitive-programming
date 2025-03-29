#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
            we run a DFS:
              worst case: 4^K .. K being the length of digits

            Space: O(K) ... since DFs
        '''
        
        map = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w','x','y','z']
        }

        combinations = []
        def generate_combination(digits, combo):
            if not digits:
                if combo:
                    combinations.append(''.join(combo))
                return
            
            letters = map.get(int(digits[0]))
            for letter in letters:
                generate_combination(digits[1:], combo+[letter])
        
        generate_combination(digits, [])
        return combinations

   
# @lc code=end

