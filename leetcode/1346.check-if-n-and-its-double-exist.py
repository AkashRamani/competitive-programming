#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dictionary = {}

        for i, val in enumerate(arr):
            isDouble = True if 2*val in dictionary else False
            isHalf = True if val%2==0 and val//2 in dictionary else False #if odd no need to, coz constraint. Plus mk sure to companre 'int' coz keys
                     
            if isDouble or isHalf:
                return True
            dictionary[val] = 1
        return False        
# @lc code=end

