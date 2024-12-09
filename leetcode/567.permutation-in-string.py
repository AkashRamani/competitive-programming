#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ''' Approach -> Find Annagram of s1 in s2 using sliding windows '''

        if len(s1)>len(s2):
            return False

        s1Count = {i:0 for i in string.ascii_lowercase}
        s2Count = {i:0 for i in string.ascii_lowercase}

        for i in range(len(s1)):
            s1Count[s1[i]] +=1
            s2Count[s2[i]] +=1 #ek baar krna hi hai when len = s1.len
        
        matches = 0 #indicates how many letter's count match range{0,26}
        for i in string.ascii_lowercase:
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            #remove from left, update count
            char = s2[left]
            s2Count[char] -=1
            if s2Count[char] == s1Count[char]:
                matches+=1
            elif s2Count[char] + 1 == s1Count[char]: # means they were equal, now unequal
                matches -=1
            #update left
            left+=1

            # Add right, update count
            char = s2[right]
            s2Count[char] +=1
            if s2Count[char] == s1Count[char]:
                matches+=1
            elif s2Count[char] - 1 == s1Count[char]: # means they were equal, now unequal
                matches -=1
        return matches ==26        
        
# @lc code=end

