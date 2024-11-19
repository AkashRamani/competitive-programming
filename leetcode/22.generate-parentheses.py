#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 'o' : count of remaining opening parentesis
        # 'c' : count of remaining closing parentesis
        #G(o,c returns the count of possible Parentheses when there are o,c --> n)
        def G(o, c, s):
            if o > c:
                return []
            if o == 0:
                if o == c == 0:
                    return [s]
                return G(0, c-1, s+')') #actually we can be certain this is the solution
            return G(o,c-1, s+')') + G(o-1, c, s+'(')

        return G(n,n, "")

        # To optimize further I can use memoization/ dynamic programming
# @lc code=end

