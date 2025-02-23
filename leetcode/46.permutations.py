#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
            Recursion:
                reduce the problem till array is empty.. return [[]]
                    At each stage:
                        grab permutations from older layer.
                        iterate through each permutation:
                            within each permuttion => insert element (first elem of array) to all possible places and record

            Time: O(N* N!) == N! == N^N ==> Linear in #of combos generated 
            Space: O(N!)  ==> To store N! permutations.. Linear in #of combos generated
        ''' 


        def generate_combos(element, perm):
            for pos in range(len(perm)+1):
                yield perm[:pos] + [element] + perm[pos:]

        def give_permutations(array):
            if not array:
                return [[]]

            permutations = give_permutations(array[1:])
            first = array[0]

            new_permutations = []
            for perm in permutations:
                new_permutations.extend(generate_combos(first, perm)) #extend: a+b <=> a.extend(b)
            return new_permutations
        return give_permutations(nums)

        # def give_permutations(array):
        #     if not array:
        #         return [[]]

        #     perms = give_permutations(array[1:])
        #     first = array[0]

        #     permutations = []
        #     for perm in perms:

        #         combos = []
        #         index = len(perm)
        #         while index>=0:
        #             perm_copy = perm.copy()
        #             perm_copy.insert(index, first) #exceptions are handled
        #             permutations.append(perm_copy)
        #             index-=1
        #     return permutations
        # return give_permutations(nums)
        
# @lc code=end

