#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        lcs = 0
        for i in range(len(nums)):
            if not nums[i]-1 in num_set:
                current_lcs = 1
                num = nums[i]
                #sum total of times, while will be iterated is n
                while num+1 in num_set:
                    num +=1
                    current_lcs+=1
                lcs = lcs if lcs>current_lcs else current_lcs
        return lcs

        #^ time O(n) ; memory: O(n) 
        #manages to solve the calculating of lcs part At an AMORTIZED COST of elment O(1)
        # Hence.. time O(n) ; space O(n)


    ## sub-optimal --> to sort and get lcs in a single pass 
    #Time O(n * log n) & Space: O(n) / O(1) : depending on the sorting algo used
        # nums.sort()
        # if not nums:
        #     return 0

        # lcs = 1
        # current_lcs = 1

        # for i in range(1, len(nums)):
        #     if nums[i-1] == nums[i]:
        #         continue
        #     if nums[i-1]+1 == nums[i]:
        #         current_lcs +=1
        #     else:
        #         lcs = max(lcs, current_lcs)
        #         current_lcs = 1

        # return max(lcs, current_lcs)


    ## Brute force is at every number: you calculate the lcs <which would take o(n^2) - n passes accross n to get lcs>
    # Time complexity: O(n^3) ; space: O(1)

    # OPTIMAL APPROACH manages to solve the calculating of lcs part At an AMORTIZED COST of elment O(1)
    # Hence.. time O(n) ; space O(n)
        
# @lc code=end

