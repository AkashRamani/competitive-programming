#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
            Heapify -- O(N)
            get-max --> O(log N) ~n times ~ O(N log N)
            insert-back --> O(log N)

            Total: O(N log N)
    
        '''
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1, stone2 = -heapq.heappop(stones), -heapq.heappop(stones)
            stone1, stone2

            stone3 = stone1-stone2

            if stone3:
                heapq.heappush(stones, -stone3)

        if len(stones):
            return -stones[0]
        return 0
# @lc code=end

