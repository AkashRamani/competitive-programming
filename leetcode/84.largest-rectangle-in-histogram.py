#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #look at neetcode's video for a good explanation, striver is good too

        stack = []
        max_area = 0

        for index, height in enumerate(heights):
            # last_height = stack[-1][1]
            popped_index = index  
            while stack and stack[-1][1] > height:
                #you need to pop.. but before that calc max-area
                popped_index, popped_height = stack.pop() #popped_index is leftmost_same_height
                width = index - popped_index
                max_area = max(max_area, width * popped_height)
            
            stack.append((popped_index, height))

        while stack:
            popped_index, popped_height = stack.pop()
            width = index - popped_index + 1
            max_area = max(max_area, width * popped_height)

        return max_area
        
# @lc code=end

