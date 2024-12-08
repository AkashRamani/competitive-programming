#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Time: O(log(len_of_smaller_array)) ; space: O(1)

        len1,len2 = len(nums1), len(nums2)
        total_len = len1+len2
        num_in_left_half = (total_len + 1)//2

        #nums1 always the smaller array
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = len1

        while low <= high:
            mid1 = (low+high) >> 1 #divide by 2; bas yuhi LOL
            mid2 = num_in_left_half - mid1

            # To ensure there is no out of bounds error
            l1, l2 = float("-inf"),float("-inf")
            r1, r2 = float("inf"), float("inf")

            if mid1 < len1:
                r1 = nums1[mid1]
            if mid2 < len2:
                r2 = nums2[mid2]
            
            if mid1 - 1 >=0: #to handle empty input array:  []
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >=0:
                l2= nums2[mid2 - 1]

            # Above few lines can be clubbed as such too..
            # l1 = nums1[mid1 - 1] if mid1 > 0 else float("-inf")
            # r1 = nums1[mid1] if mid1 < len1 else float("inf")
            # l2 = nums2[mid2 - 1] if mid2 > 0 else float("-inf")
            # r2 = nums2[mid2] if mid2 < len2 else float("inf")

            #Actual Binary search ke conditions
            if l1<=r2 and l2 <=r1:
                if total_len%2:
                    return max(l1,l2)
                return (max(l1,l2) + min(r1, r2))/2
            
            elif l1>r2:
                high = mid1-1
            else:
                low = mid1+1
        return 0


# @lc code=end

