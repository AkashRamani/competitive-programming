#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        solution = []
        def dfs(i, cur_sum, subarray):
            if cur_sum == target:
                solution.append(subarray[:])
                return

            for index in range(i, len(candidates)): # we use this to skip same digits
                if index >= len(candidates):
                    return
                if index > i and candidates[index] == candidates[index - 1]:
                    continue
                if cur_sum + candidates[index] > target:
                    return
                
                dfs(index + 1, cur_sum + candidates[index], subarray + [candidates[index]])
    
        dfs(0, 0, [])
        return list(solution)
# @lc code=end

