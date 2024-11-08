#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = dict()
        # compare lengths and do an early return
        for i in s:
            if not i in hash:
                hash[i] = 0
            hash[i] = hash[i]+1

        for i in t:
            if not i in hash:
                return False
            hash[i] = hash[i]-1
            if hash[i] < 1:
                del hash[i]
        if len(hash.keys()):
            return False
        return True
    
# @lc code=end

