#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0

        maxLen = 0
        chars = dict()
        while j < len(s):
            if s[j] in chars:
                dup_index = chars[s[j]]
                if dup_index >= i: #could be a stale value, so a check if dup is in our bounds of current i,j
                    i = dup_index+1

            chars[s[j]] = j
            maxLen = max(j-i+1, maxLen)
            j+=1

        return maxLen
        
# @lc code=end

