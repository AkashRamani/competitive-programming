#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            if not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left +=1
                right -=1
        return True
    
class Solution1:
    '''
        Author: Aniket Patel
    '''
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""

        for x in s:
            if x.isalnum():
                clean_s += x.lower()

        left = 0
        right = len(clean_s) - 1
        
        while(left < right):
            if clean_s[left] == clean_s[right]:
                left += 1
                right -= 1
            else:
                return False
            
        return True
            
sol = Solution1()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))

# @lc code=end

