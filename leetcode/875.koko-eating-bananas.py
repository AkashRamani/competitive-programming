#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
            idea is to run binary search on k values and find the inflection point where.. 
            i.e: Find k, where it changes from not-possible-to-finish to finish.


            Notice: For a given value of k, irrespective of the order within pile, it will take same time.
        '''

        def finish_all_bananas(piles, hours,rate):
            if rate<1:
                return 0

            for pile in piles:
                if hours < 0:
                    return 0
                hours = hours - math.ceil(pile/rate)

            return hours >= 0


        '''
        Imagine an array of k.. with  [0,1,2,3...,max(piles)]
        But look at it like this [T,T,T,F,F....,F,F,F,F] we want to find the inflection point
        https://youtu.be/tgVSkMA8joQ?si=D8gYpxDN3UKgmWiK&t=193
        NOTICE in video at Time 5:50 
 
        But the distinction is -- I am directly plaing with values of k. contrary to indexes in the video (so dont confuse)
        '''

        low = 0
        high = max(piles)
        
        while low < high:
            mid = (low+high)//2

            if finish_all_bananas(piles, h, mid):
                high = mid
            else:
                low = mid+1
        return low


# @lc code=end

