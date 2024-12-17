#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        chars = [0 for i in range(26)]
        sum = 0

        for char in sentence:
            char_index = ord(char) - ord('a')

            if not chars[char_index]:
                chars[char_index] +=1
                sum +=1
        return sum>25

        
# @lc code=end

