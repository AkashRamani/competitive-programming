#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # recursion
        def loot(i):
            if not (0<=i<len(nums)):
                return 0
            return max(nums[i]+ loot(i+2), loot(i+1))
        return loot(0)
    
class Solution2:

    def rob(self, nums: List[int]) -> int:
        # Memoization [top-down/bottom up?]
        table = [-1 for _ in nums]

        def loot(i):
            if not (0<=i<len(nums)):
                return 0
            if table[i] != -1:
                return table[i]
            
            loot_amount = max(cost[i]+ loot(i+2), loot(i+1))
            table[i] = loot_amount
            return loot_amount
        return loot(0)
        
# @lc code=end

