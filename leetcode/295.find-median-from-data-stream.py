#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
class MedianFinder:
    '''
        Did a few extra things in first itertations: which can be avoided hence second iteration..

        Idea: 
            Maintian 2 heaps, 
            > first heap --> maintain values lower than median, in a max heap
                         --> Allow it to have one number greater than second heap if required
            > second heap --> maintain values higher than median, in a min heap
        Top can be used to compute median

        Complexity:
            1. AddNum: 
                Time: O(log N) --> For heap insertions/deletion --at max 3 such operations of time  O(log N)
                Space: O(N) -- for 2 hash map
            2. Find Median:
                Time: O(1) -- const time.. simply lookup heap tops
                Space: O(1) -- const space
    '''

    def __init__(self):
        self.first_half = [] #max-heap
        self.second_half = [] #min-heap

    def addNum(self, num: int) -> None:
        if len(self.first_half) == len(self.second_half):
            heapq.heappush(self.second_half, num)
            heapq.heappush(self.first_half, -heapq.heappop(self.second_half))
        else:
            heapq.heappush(self.first_half, -num)
            heapq.heappush(self.second_half, -heapq.heappop(self.first_half))          

    def findMedian(self) -> float:
        if len(self.first_half) == len(self.second_half):
            return (-self.first_half[0] + self.second_half[0]) / 2
        else:
            return -self.first_half[0]
            
class MedianFinder2:
    def __init__(self):
        self.first_half = [] #max-heap
        self.second_half = [] #min-heap

    def addNum(self, num: int) -> None:
        if not self.first_half:
            self.first_half.append(-num)
            return
        if not self.second_half:
            self.second_half.append(num)
            if num < -self.first_half[0]:
                self.first_half, self.second_half = self.second_half, self.first_half
                self.first_half = [-i for i in self.first_half]
                self.second_half = [-i for i in self.second_half]
            return

        if num <= -self.first_half[0]:
            heapq.heappush(self.first_half, -num)
        else:
            heapq.heappush(self.second_half, num)

        if len(self.second_half) > len(self.first_half):
            popped_num = heapq.heappop(self.second_half)
            heapq.heappush(self.first_half, -popped_num)
        
        if len(self.first_half) > len(self.second_half)+1:
            popped_num = heapq.heappop(self.first_half)
            heapq.heappush(self.second_half, -popped_num)
        return

    def findMedian(self) -> float:
        if not self.second_half:
            return -self.first_half[0] # at least one element in, before calling findMedian

        if len(self.first_half) == len(self.second_half):
            return (-self.first_half[0] + self.second_half[0])/2
        else:
            return -self.first_half[0] 



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

