#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #Sort and do it..
        # For loop becuase:
        #    we want to skip donot include: when duplicates - coz they will be already be included and will result in duplicates 
        # Time: 
        #   sort - O(N)
        #   for loop runs to increment i.. so over all the iteratons it will tk O(N)
        #         ... is it? If the array is filled with duplicates.. then it will keep running from i till end
        #           ...so worst worst case: N * cost_of_recursion
        #   cost of recursion ~ (2^N )    
        
        #   TOTAL ==>  O(N* O(log N))

        solution = []

        def dfs(i, curr_set):
            if i >= len(nums):
                solution.append(curr_set.copy())
                return
            
            dfs(i+1, curr_set + [nums[i]]) #include
            
            for index in range(i, len(nums)):   
                if index > i and nums[i] == nums[index]: 
                    i+=1

            dfs(i+1, curr_set) # dont include

        nums.sort()
        dfs(0, [])
        return list(solution)
# @lc code=end

