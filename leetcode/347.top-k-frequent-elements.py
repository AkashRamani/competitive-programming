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
    
class Solution2:
    '''
    Implemented using a heap.
    Builds a max heap by ensuring each parent node is larger than its children.
    
    Author: Aniket
    '''
    def build_heap(self, heap: List[int], index) -> List[int]:
        if index == 0:
            return heap
        if index % 2 == 0:
            parent_index = (index - 2) // 2
            if heap[parent_index] < heap[index]:
                heap[parent_index], heap[index] = heap[index], heap[parent_index]
                heap = self.build_heap(heap, parent_index)
        else:
            parent_index = (index - 1) // 2
            if heap[parent_index] < heap[index]:
                heap[parent_index], heap[index] = heap[index], heap[parent_index]
                heap = self.build_heap(heap, parent_index)
              
        return heap
    
    def heapify(self, heap: List[int], index) -> List[int]:
        if index == 0:
            return heap
        if index % 2 == 0:
            parent_index = (index - 2) // 2
            if heap[parent_index] < heap[index]:
                heap[parent_index], heap[index] = heap[index], heap[parent_index]
                heap = self.build_heap(heap, parent_index)
        else:
            parent_index = (index - 1) // 2
            if heap[parent_index] < heap[index]:
                heap[parent_index], heap[index] = heap[index], heap[parent_index]
                heap = self.build_heap(heap, parent_index)
        
        return heap

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        counter_dict = dict(counter)   # Get frequency of each element
        conter_values = counter_dict.values()
        conter_values_list = list(conter_values)
        heap = []
        most_occuring = []
        ans = []

        for i in range(0, len(conter_values_list)):
            heap.append(conter_values_list[i])
            heap = self.build_heap(heap, i)

        if len(heap) == 1:
            for k,v in counter_dict.items():
                return [k]
            
        for i in range(0,k):
            heap[0], heap[-1] = heap[-1], heap[0]
            most_occuring.append(heap.pop())
            if len(heap) == 0:
                break
            for i in range(len(heap)-1,-1,-1):
                heap = self.heapify(heap, i)
            # heap = self.heapify(heap, len(heap)-1)

        for key in most_occuring:
            for k,v in counter_dict.items():
                if v == key:
                    ans.append(k)
                    del counter_dict[k]
                    break

        return ans
      
# @lc code=end

