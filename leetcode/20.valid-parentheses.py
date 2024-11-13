#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        #Next time encountering this quesiton implement your own stack will all necessary methods and use it

        #Time: O(n); Space: O(n) -- stack
        hash_brackets = {'(':')', '{':'}', '[': ']'}
        stack = []
        for char in s:
            if char in hash_brackets:
                stack.append(char)
            elif char in hash_brackets.values():
                if len(stack)>0 and char == hash_brackets[stack[-1]]:
                    stack.pop()
                else:
                    return False
                    
        if len(stack) == 0:
            return True
        return False
        
# @lc code=end

