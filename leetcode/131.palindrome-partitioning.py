#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
            Time:
              O(N * 2^N) : 
               O(N) -- for pallindrome
               O(2^N) -- there is a decision to 
        '''

        answer = []

        map = {}
        def check_palindrome(i,j):
            if i>j:
                return False
            if (i,j) in map:
                return map.get((i,j))
            while i < j:
                if s[i] != s[j]:
                    map[(i,j)] = False
                    return False
                i+=1
                j-=1

            map[(i,j)] = True
            return True

        def partition(i, j,pieces):
            if i==len(s):
                answer.append(pieces.copy())
                return
            for index in range(i, len(s)):
                part1= s[i:index+1]
                if check_palindrome(i, index):
                    partition(index+1, j, pieces+ [part1])

        partition(0, len(s), [])
        return answer




        
        # answer = []

        # def check_palindrome(s):
        #     if not s:
        #         return
        #     i = 0
        #     j = len(s)-1

        #     while i < j:
        #         if s[i] != s[j]:
        #             return False
        #         i+=1
        #         j-=1
        #     return True

        # def partition(s,pieces):
        #     if not s:
        #         answer.append(pieces.copy())
        #         return

        #     for i in range(0, len(s)):
        #         part1, part2 = s[:i+1], s[i+1:]
        #         if check_palindrome(part1):
        #             partition(part2, pieces+ [part1])

        # partition(s, [])
        # return answer 
# @lc code=end

