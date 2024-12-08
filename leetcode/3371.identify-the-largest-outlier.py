# @lc code=start
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        dictionary = {}
        for index, num in enumerate(nums):
            if not num in dictionary:
                dictionary[num] = set()
            dictionary[num].add(index)

        outlier = -1001

        for index, num in enumerate(nums):
            sum_wo_outlaier = sum_nums - num
            indexes = dictionary.get(sum_wo_outlier//2, {})

            if sum_wo_outlier%2==0 and indexes and (index not in indexes or index in indexes and len(indexes)>1):
                    outlier = max(outlier, num)
        return outlier