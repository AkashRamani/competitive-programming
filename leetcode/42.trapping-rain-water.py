#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:

        '''
        O(n) Space and O(n) Time...
        idea is to maintain 2 arrays.. such that at every index: 
        We know what is the max height from left and max height from right..
        and once we know that, amt at that index can be:
             min(left ht, right ht) - h[i]. {since h[i] is occupied by topography. land already}
         '''
        n=len(height)
        maxLeft = [0 for i in range(n)]
        maxRight = [0 for i in range(n)]

        total_water = 0

        max_height = 0
        for i in range(n):
            max_height = max(max_height, height[i])
            maxLeft[i] = max_height
        
        max_height = 0
        for i in range(n-1, -1, -1):
            max_height = max(max_height, height[i])
            maxRight[i] = max_height

        for i in range(n):
            amount_of_water_stored_at_i = min(maxLeft[i], maxRight[i]) - height[i]
            total_water +=amount_of_water_stored_at_i
        return total_water
        
# @lc code=end

