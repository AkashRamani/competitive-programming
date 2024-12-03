#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        My idea ... apply binary search to get from where it's roated (can be done in O(logn))
        Then split the array in two.. and perform searches <Vaha pe time complexity will be 
        O(logK + log n-K) where 1<=k<=n
        '''
        '''
        "This is S30 ka, mera approach is below.. but this one's simple , easy and affective!"

        Idea is.. one from mid : either left half or right half will be sorted. 
        We will try to search for the value in sorted half and adjust low, high accordingly
        '''

        if len(nums)==0: return -1 
        low=0
        high=len(nums)-1
        
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[low]<=nums[mid]:     #Matlab Left to mid sorted
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:                          #Matlab right side sorted
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1
            
        
        
        
        
        
        
'''
        def binarysearch(low, high, target):
            if low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    return mid
                elif target<nums[mid]:
                    return binarysearch(low, mid-1, target)
                elif target>nums[mid]:
                    return binarysearch(mid+1, high, target)
            return -1
        
        def findpivot(low,high):
            print("--",low,high,"--")
            # if nums[low]<nums[high]:
            #     return -1               #Arrray is pura sorted
            if low>=high:
                return high
            if low+1==high:
                if nums[low]>nums[high]:
                    print("a")
                    return low
                else:
                    print("b")
                    return high
            mid=(low+high)//2
            if nums[mid]<nums[low]:
                print(1)
                return findpivot(low, mid)
            elif nums[mid]>nums[high]:
                print(2)
                return findpivot(mid,high)
            print("idhar")
            return -1
            
        low=0
        high=len(nums)-1
        
        pivot=findpivot(low, high)
        print("pivot",pivot)
        if pivot==-1:                    #Array sorted
            return binarysearch(low, high, target) 
        if pivot==0:
            if target==nums[0]:
                return 0
            else:
                return binarysearch(pivot+1, high, target)
        else:                           # 0 till pivot, pivot+1 till max len
            r1=binarysearch(low, pivot, target)
            r2=binarysearch(pivot+1, high, target)
            print(r1,r2)
            return max(r1,r2)
        
#         #Ye bakchodi karni padti agar finite length hoti... isme directly pivot find kardo yaar
        
#         while high < 2*int(math.log(len(nums),2)):
#             if nums[low]<nums[high]:
#                 if nums[low]<target<nums[high]:
#                     return binarysearch(low, high, target)
#                 else:
#                     low=high
#                     high=high+1
#             else:
#                 find pivot()
#                 binary search...
#         return -1
'''
        
# @lc code=end

