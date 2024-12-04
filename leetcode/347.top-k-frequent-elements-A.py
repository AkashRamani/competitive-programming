from typing import List
from collections import Counter

class Solution:
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

ans = Solution().topKFrequent([4,1,-1,2,-1,2,3], 2)
print(ans)