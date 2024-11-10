#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        '''
         Note.: [[-1,-1,2]] is allowed but NOT [[-1,-1,2], [-1,-1,2]]

         Time: O(n^2); space: O(1) -- ofcourse not considering output array
        '''
        
        ans = []
        nums.sort()

        #move right ptr to the next unique number - to avoid dup solutions
        def move_right_pointer(nums, index):
            num = nums[index]
            while index>0 and nums[index] == num:
                index-=1
            return index

        #move left ptr to the next unique number
        def move_left_pointer(nums, index):
            num = nums[index]
            while index < len(nums)-1 and nums[index] == num:
                index+=1
            return index
        
        i=0
        while i < len(nums)-2:
            left = i+1
            right = len(nums)-1
            while i < left < right:
                if nums[left]+nums[right]+nums[i]>0:
                    #move right ptr
                    right = move_right_pointer(nums, right)

                elif nums[left]+nums[right]+nums[i]<0:
                    #move left ptr
                    left = move_left_pointer(nums, left)
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    # after a sol, move left and right
                    right = move_right_pointer(nums, right)
                    left = move_left_pointer(nums, left)
            #move i
            i = move_left_pointer(nums, i)

        return ans



        '''
            This is optimal solution I submitted in Feb'23. Lousy way/ bad way of writing the optimal soution.
            The new code is more readable and logically makes sense
        '''
        # ans=[]
        # nums.sort()
        # for i in range(len(nums)-2):
        #     l=i+1
        #     h=len(nums)-1
        #     if i>0 and nums[i-1]==nums[i]:
        #         continue
        #     while l<h:
        #         # if nums[l-1]== nums[l]: #or nums[i]==nums[l]:
        #         #     l+=1
        #         # elif h<len(nums)-1 and nums[h+1]==nums[h]:
        #         #     h-=1
        #         if nums[i]+nums[l]+nums[h] > 0:
        #             h-=1
        #         elif nums[i]+nums[l]+nums[h] < 0:
        #             l+=1
        #         else:
        #             ans.append([nums[i], nums[l], nums[h]])
        #             l+=1
        #             while nums[l-1]== nums[l] and l<h: #or nums[i]==nums[l]:
        #                 l+=1
        #             h-=1
        # return ansa
# @lc code=end

