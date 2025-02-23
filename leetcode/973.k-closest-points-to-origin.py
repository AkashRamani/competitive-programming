#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
            Time: 
            Heapify k points --> O(log k)
            For ~n points: each insert takes ~ O(log k) ==> O (N log K)

            Space:
            My code has space of O(k) --> size of heap
        '''
        distances = [(-1*(pow(a,2)+pow(b,2)), [a,b]) for a,b in points[:k]]
        heapq.heapify(distances)

        for a,b in points[k:]:
            distance = pow(a,2)+pow(b,2)
            if distance < -distances[0][0]:
                heapq.heappushpop(distances, (-distance, [a,b]))
            
        return [point for dist, point in distances]
# @lc code=end

