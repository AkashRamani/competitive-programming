#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        idea/though process
            4,  5,  1,  2
        0   1      *    5*1*2
        1   4      *    1*2
        2   4*5    *    2
        3.  4*5*1  *    1

        '''

        l = [0 for i in range(0, len(nums))] 
        r = [0 for i in range(0, len(nums))]

        mul = 1
        for i, num in enumerate(nums):
            l[i] = mul
            mul *= num 
        
        mul = 1
        for i in range(len(nums)-1, -1, -1):
            r[i] = mul
            mul *=nums[i]

        output = []
        for i in range(0, len(nums)):
            output.append(l[i]*r[i])

        return output
# @lc code=end

