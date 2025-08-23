#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(i, j):
            if 0>i>=len(s) and 0>j>=len(s):
                return False

            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True



        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return check_palindrome(i+1, j) or check_palindrome(i, j-1)
            i+=1
            j-=1
            
        return True
# @lc code=end

