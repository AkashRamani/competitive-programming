#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        def back_track(subset, array):
            ans.add(subset)
            for i,elem in enumerate(array):
                new_sub_set = subset+(elem,)
                back_track(new_sub_set, array[i+1:])

        back_track((), nums)
        return [list(i) for i in list(ans)]

        
# @lc code=end

