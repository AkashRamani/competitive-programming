#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # word_len = 0
        # word_encountered = 0

        # i = len(s)-1
        # while i >= 0:
        #     if s[i] == " " and word_encountered:
        #         break
        #     if s[i] != " ":
        #         word_encountered = 1
        #         word_len+=1
        #     i=i-1
        # return word_len


        ''' Now I can remove the flag `word_encountered`. Becuase we can get the same info by knowing if word_len > 0 '''
        word_len = 0

        i = len(s)-1
        while i >= 0:
            if s[i] != " ":
                word_len+=1
            elif word_len:  #Note -  s[i] == " " -- is implicit so can be ignored
                break
            i=i-1
        return word_len

        
# @lc code=end

