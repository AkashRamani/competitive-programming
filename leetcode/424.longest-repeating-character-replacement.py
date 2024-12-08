#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
            Time: O(n) ; Space O(1)

            But note that compared to solution vv:
                Downgrading frequencies shortening the window using while is redundant in this case, becuase we are only concerend with Max Frequencies! Hence an updated solution
                https://youtu.be/_eNhaDCr6P0?si=9Q5RwywWUpgWYJBb&t=1192

        '''
        i,j = 0,0

        maxL, maxF = 0, 0
        chars = {letter: 0 for letter in string.ascii_uppercase}

        while j < len(s):
            chars[s[j]] += 1
            maxF = max(maxF, chars[s[j]])

            if (j-i+1) - maxF > k: 
                chars[s[i]] -=1
                i+=1

            if (j-i+1) - maxF <= k:
                maxL = max(maxL, j-i+1)

            j+=1

        return maxL

        '''
            Time: O(n) ==> the second while loop has an amortized/total cost of O(N) ; Space: constant
        ''' 
        # i,j = 0,0

        # maxL, maxF = 0, 0
        # chars = {letter: 0 for letter in string.ascii_uppercase}

        # while j < len(s):
        #     chars[s[j]] += 1
        #     maxF = max(maxF, chars[s[j]])

        #     while (j-i+1) - maxF > k:  #this can be safely elimiated
        #         chars[s[i]] -=1
        #         maxF = 0
        #         for char, freq in chars.items():  #this can be safely eliminated
        #             maxF = max(maxF, freq)
        #         i+=1

        #     if (j-i+1) - maxF <= k:
        #         maxL = max(maxL, j-i+1)

        #     j+=1

        # return maxL
                

        
# @lc code=end

