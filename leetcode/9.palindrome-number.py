#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        ''' reversing might give int overflow error.. so come up with a solution for this next time'''
        if x<0:
            return False
        
        temp = x
        rev = 0
        while (temp): 
            rev=rev*10+(temp%10)
            temp = temp//10
        return x == rev
        
# @lc code=end

