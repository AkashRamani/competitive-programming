#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ''' Approach -> Sliding window with deque 
        
        1. Use deque to store indices of elements in the window.
        2. Use two pointers i and j for window's start and end.
        3. Maintain a list to store maximum values in the window.
        
        Author - Akash
        '''
        i, j = 0, 0
        queue = collections.deque()

        out = []
        while j < len(nums):
            while queue and nums[queue[-1]] < nums[j]: #while smaller vlaues in queue pop from queue
                queue.pop()
            queue.append(j)

            if i > queue[0]:
                queue.popleft()

            if (j+1) >= k:
                out.append(nums[queue[0]])
                i+=1
            j+=1
        return out
        
# @lc code=end

