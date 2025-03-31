#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            DP -- bottom up
        '''
        if n<=2:
            return n
        ways = [-1]*(n+1)
        ways[1] = 1
        ways[2] = 2

        for i in range(3, n+1):
            ways[i] = ways[i-1]+ways[i-2]
        return ways[n]


        '''
            Memoization.. Top-down DP
        '''
        ways = [-1]*(n+1)
        def steps(n):
            if n<1:
                return 0
            if n==1:
                return 1
            if n==2:
                return 2
            if ways[n] != -1:
                return ways[n]
            total_steps = steps(n-1)+steps(n-2)
            ways[n] = total_steps
            return total_steps
        return steps(n)



        '''
            Recursive --TLE
        '''
        def steps(n):
            if n<1:
                return 0
            if n==1:
                return 1
            if n==2:
                return 2
            return steps(n-1)+steps(n-2)
        return steps(n)

    



# @lc code=end

