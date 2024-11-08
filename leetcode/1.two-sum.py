#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = dict()

        for i, number in enumerate(nums):
            if number in store:
                return [store[number], i]
            store[target - number] = i

        #simple hai.. (target- number): index_of_number store karo.. Jabh dusra number == key mile toh woh store[number], i are solutions 
# @lc code=end

