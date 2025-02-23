#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
            > at every element you have a choice to include element or not.
            > Imagine that as a tree and the leaves of it are the power-set
            > There would be 2^N nodes

            Time complexity is 2^N

            We are doing DFS.. so space is o(log N)
        '''
        solution = []
        def dfs(i, sub_array):
            if i >= len(nums):
                solution.append(sub_array)
                return 
            dfs(i+1, sub_array) #dont-take
            dfs(i+1, sub_array + [nums[i]] ) #take

        dfs(0, [])
        return solution

class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # This is bad
        ans = set()
        def back_track(subset, array):
            ans.add(subset)
            for i,elem in enumerate(array): # this is bad way to write it LOL
                new_sub_set = subset+(elem,)
                back_track(new_sub_set, array[i+1:])

        back_track((), nums)
        return [list(i) for i in list(ans)]

class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
            Using a bit mask.. think of this.. binary number says whether to include element or not
            Time complexity is 2^N
            Space complexity is 2^N
        '''
        sub_set = []
        for i in range(2**len(nums), 2**(len(nums)+1)):
            bitmask = bin(i)[3:]
            print(bitmask)
            sub_set_element = []
            for j, val in enumerate(bitmask):
                if val == '1':
                    sub_set_element.append(nums[j])
            sub_set.append(sub_set_element)

        return sub_set
        
# @lc code=end

