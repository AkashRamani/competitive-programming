#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ''' Think of this problem as insert at thevery first occurance 
            Refer - https://youtu.be/tgVSkMA8joQ?si=AEFtq8hffqra-G5S&t=164
        '''


        left = 0
        right = len(nums)

        while left < right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
        
# @lc code=end

