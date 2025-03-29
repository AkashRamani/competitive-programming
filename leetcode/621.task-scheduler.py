#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
            Time: 
            heapify -- O(n)

            getMax       -  N log N
            push to heap - N log N
            -----------------------
            Total: N log N

            Space: size of queue : O(n)
        '''
        counts = [0 for i in range(26)]
        for task in tasks:
            index = ord(task)-ord('A')
            counts[index]+=1

        i = 0    
        for count in counts:
            if count>0:
                counts[i] = -count
                i+=1
        counts = counts[:i]

        heapq.heapify(counts)
        queue = deque()

        time = 0
        
        while len(counts) or len(queue):
            time=time+1
            if len(queue):
                q_count,q_time = queue[0]
                if q_time == time:
                    q_count,q_time = queue.popleft()
                    # Add in heap
                    heapq.heappush(counts, q_count)

            if len(counts):
                count = -1*heapq.heappop(counts)
                count -=1
                if count: #append to heap at time t+n
                    queue.append((-count, time+n+1))

            
            
        return time
            
# @lc code=end

