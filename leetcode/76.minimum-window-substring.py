#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        '''
            Sliding window.. 
            Increment j till you find a matching substring.
            As soon as you find one, increment i, to minimize the window, 
            As you are increasing i, check if condition holds. 
            As soon as you hit substring to be not satisfying.. pause i
            And start with incrementing j again. Till you exaust j.

            To easily check if counts in both dictionaries match use variable `have` and `need`. Code is intutive.
            But just in case: https://www.youtube.com/watch?v=jSto0O4AJbM
        '''

        i, j = 0, 0

        char_map = {}
        str_map = {} 
        for char in t:
            if not char in char_map:
                char_map[char] = 0
                str_map[char] = 0
            char_map[char] += 1

        need = len(char_map)
        have = 0

        min_len = float("inf")
        solution = ""
        while j < len(s):

            char = s[j]
            if char in char_map:
                # add j
                if str_map[char] +1 == char_map[char]:
                    have+=1

                str_map[char] += 1

         
            while have == need:    
                if (j-i+1) < min_len:
                    solution = s[i:j+1]
                    min_len = len(solution)

                char = s[i]
                if char in char_map:
                    #remove i

                    if str_map[char] == char_map[char]:
                        have -=1
                    str_map[char] -= 1

                i+=1
            j+=1
                
        return solution
        
# @lc code=end

