#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        # Can be done in n. log (n) if we use binary search
        # but hash map willdo it in O(n). yes! but space is O(n) too ://

        # The fact that it is sorted we can use two pointer approach and get get to a solution 
        # (since it has a unique solution)
        #O(n) time and O(1) space 

        left = 0
        right = len(numbers)-1

        while left < right:
            if numbers[left]+numbers[right] > target:
                right-=1
            elif numbers[left]+numbers[right] < target:
                left+=1
            else:
                return [left+1, right+1]
        
        
# @lc code=end

