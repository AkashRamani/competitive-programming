#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        Based on deeper analysis of Fllyd's cycle detection algo, 
        here we not only detect the cycle, we point out the node that forms a cycle.

        Explanation by neetcode : https://www.youtube.com/watch?v=wjYnzkAhcNk
        '''

        slow, fast =0,0 

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] #think of this as moving two pointers
        
            if fast == slow:
                break
        
        slow2 = 0
        #increment slow and slow2 till they meet
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                break
                
        return slow

        '''
        Another slick trick: we mark the index corresponding to N-1 as negative, 
        if we encounter a negative index again it means we have looked at it once!!!
        '''

        for num in nums:
            index = abs(num) -1

            if nums[index] < 0:
                return abs(num)
            
            nums[index] = -1*nums[index]

# @lc code=end

