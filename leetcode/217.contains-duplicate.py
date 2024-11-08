#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map =dict()

        for number in nums:
            if not number in hash_map:
                hash_map[number] = 1
            else:
                return True
        return False
    #You can use set too..  hash_map = set() and hash_map.add(number)
    
# @lc code=end

