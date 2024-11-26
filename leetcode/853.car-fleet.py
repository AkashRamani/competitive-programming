#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Time : O(nlogn) -- to sort; 
        #Space: O(n) if we use stack -- but we can use a counter instead. And there can be a clean way to sort speed array with position 

        speed_at_pos = {}
        #since positions are unique
        for i in range(len(speed)):
            speed_at_pos[position[i]] = speed[i]

        position.sort()

        stack = []
        for i in range(len(position)-1, -1, -1):

            distance = target - position[i]
            velocity = speed_at_pos[position[i]]
            time = distance/velocity

            if not len(stack): #first car/fleet
                stack.append(time)
            elif time > stack[-1]:  # this will never interscet with car/fleet ahead, so this is a new fleet. All cars after this can join this fleet or create a new one! 
                stack.append(time)
            else:
                # it means the cars intersects with the fleet in-front of it, before it reaches the destination. 
                # hence this can be considered a part of the same fleet, so NO append
                pass
        return len(stack)      
# @lc code=end

