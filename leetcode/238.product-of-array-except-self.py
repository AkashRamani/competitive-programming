#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Solution2 ==> Time O(n); Space O(1)

        NOTE - Description says, the output array does not count as extra space for space complexity analysis
        This is essentially Solution1 implemented with optimal use of memoery,

        '''
        out = [0 for i in range(0, len(nums))]

        mul = 1
        for i, num in enumerate(nums):
            out[i] = mul
            mul *= num
        
        mul = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i] * mul
            mul *=nums[i]

        return out


        '''
        ###########################################################
        Solution1 ==> Time O(n); Space O(n)
        idea/though process
            4,  5,  1,  2
        0   1      *    5*1*2
        1   4      *    1*2
        2   4*5    *    2
        3.  4*5*1  *    1

        '''

        # l = [0 for i in range(0, len(nums))] 
        # r = [0 for i in range(0, len(nums))]

        # mul = 1
        # for i, num in enumerate(nums):
        #     l[i] = mul
        #     mul *= num 
        
        # mul = 1
        # for i in range(len(nums)-1, -1, -1):
        #     r[i] = mul
        #     mul *=nums[i]

        # output = []
        # for i in range(0, len(nums)):
        #     output.append(l[i]*r[i])

        # return output

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Solution2 ==> Time O(n); Space O(1)

        NOTE - Description says, the output array does not count as extra space for space complexity analysis
        This is essentially Solution1 implemented with optimal use of memoery,

        '''
        
        ans = []
        post_prod = 1

        if len(nums) > 1:
            left_index = 1
            right_index = len(nums) - 2

            for i in range(left_index, len(nums)):
                ans.append(ans[-1]*nums[i-1])

            for i in range(right_index,-1,-1):
                post_prod = post_prod * nums[i+1]
                ans[i] = post_prod * ans[i-1]

            return ans
        
        return nums

# @lc code=end
