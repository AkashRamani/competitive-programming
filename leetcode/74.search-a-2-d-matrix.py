#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        '''NOW;; in this approach.. notice that when the target lis in 1st or last column.. that is our worst case..
        If we early return them 
        while we check for this.. if matrix[mid][0] <= target <= matrix[mid][right]:
    
        we can further optimize this..
        '''

        up = 0
        down = len(matrix)-1

        left = 0
        right = len(matrix[0])-1
        mid = -1

        while up <= down:
            mid = (up+down)//2
            if matrix[mid][0] <= target <= matrix[mid][right]:
                break
            if target < matrix[mid][0]:
                down = mid - 1
            elif target > matrix[mid][0]:
                up = mid+1

        if mid == -1: 
            return False
        
        while left <= right:
            center = (right+left)//2

            if target > matrix[mid][center]:
                left = center+1
            elif target < matrix[mid][center]:
                right = center-1
            else:
                return True

        return False   
# @lc code=end

