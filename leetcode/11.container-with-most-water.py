#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Time O(n); Space: O(1)
        left = 0
        right = len(height)-1
        max_area = 0

        while left < right:
            max_area = max(max_area, min(height[left], height[right])*(right-left))
        
            if height[left] < height[right]:
                left+=1
            elif height[left] > height[right]:
                right-=1
            # curr heights equal, check the upcoming height (optional to do this)
            elif height[left+1] < height[right-1]:
                left+=1 
            else:
                right-=1


        return max_area

        #Brute force is O(n^2)-
        
# @lc code=end

