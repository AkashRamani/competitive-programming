#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
            Time: O(n log k)

            Space: we use a new array for min_heap -- so O(n)
        '''

        min_heap = nums[:k]
        # min heap
        heapq.heapify(min_heap)  #O(k)

        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num) #n time O(k)
        return min_heap[0]
        
# @lc code=end

