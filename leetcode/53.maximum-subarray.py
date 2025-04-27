#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        '''
            Using Kadane's
            
            Time - O(n) - you iterate only once
            Space - O(1) 

            You maintiain a curr_sum (if its -ve, you dont carry it)
            maintian a max_value
        '''

        cur_sum = 0
        max_val = float("-inf")

        for i, num in enumerate(nums):
            max_val = max(max_val, cur_sum+num)
            cur_sum = cur_sum+num

            if cur_sum < 0:
                cur_sum = 0
            
        return max_val


        '''
            To store get the sub-array
        '''        
        cur_sum = 0
        max_val = float("-inf")

        start = 0
        end = 0
        for i, num in enumerate(nums):
            if cur_sum+num > max_val:
                max_val = cur_sum+num
                end = i 

            cur_sum = cur_sum+num

            if cur_sum < 0:
                cur_sum = 0
                start = i+1
                end = i+1
            
        print(start, end)
        return max_val
# @lc code=end

