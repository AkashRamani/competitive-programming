#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # This is O(n)

        hash_map = defaultdict(int)
        #counts for each number
        for num in nums:
            hash_map[num] +=1

        # get a bucket with length = len(nums); max_element_count !> len(nums)
        # index of bucket represents counts and value at that index represents array of elements
        bucket = [[] for i in range(len(nums)+1)] # I want to match count and index
        for num in hash_map.keys():
            count = hash_map[num]
            bucket[count].append(num)

        #iterate ulta --> coz we want higher first, till k elements are reached
        output = []
        index = len(nums)
        while k>0:
            if bucket[index] == []:
                index-=1
                continue
            output = output + bucket[index]    # We can do this because question says:guaranteed that the answer is unique. (i.e: cannot so happen ki 2 values mein se ek reh jayega)
            k-= len(bucket[index])
            index-=1

        return output
      
# @lc code=end

