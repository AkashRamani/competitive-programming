#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #This is O(n).. but not a clean code..
        # idea is to iterate backwards, from there you check and make hops to next index to check..
        # but Amortized number of hops/checks will be O(n)
        # So over all time: O(n) ;; space : O(1) --> No stack -- we are using the indexes of solution to navigate..
        
        #Since I used recursion -- it is a stack -- space is O(n) :// . use for loop instead of recursion -- space: O(1)>>

        solution = [0 for i in range(len(temperatures))]

        def check(val, index, s):
            if val < temperatures[index]:
                return s
            if val >= temperatures[index]:
                if solution[index] == 0:  #even in all decreasing temperature you will make just ONE comparison
                    return 0
                return check(val, index+solution[index], s+solution[index])

        for i in range(len(temperatures)-2, -1, -1):
            if temperatures[i+1] > temperatures[i]:
                solution[i] = 1
            if temperatures[i+1] <= temperatures[i]:
                solution[i] = check(temperatures[i] ,i+1, 1)
        return solution
# @lc code=end

