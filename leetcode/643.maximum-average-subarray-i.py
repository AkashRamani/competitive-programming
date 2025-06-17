#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''
            Time: O(n)
            Space: O(1)
        '''

        cur_sum = sum(nums[:k])
        max_sum = cur_sum

        for i in range(k, len(nums)):
            cur_sum = cur_sum + nums[i] - nums[i-k]
            max_sum = max(cur_sum, max_sum)
        return max_sum/k


        # we dont need to tk avg at each step
        cur_sum = 0
        for i in range(k):
            cur_sum += nums[i] 

        max_avg = cur_sum/k

        left = 0
        for right in range(k, len(nums)):
            cur_sum = cur_sum - nums[left] + nums[right]
            max_avg = max(max_avg, cur_sum / k)
            left+=1

        return max_avg
        
# @lc code=end

