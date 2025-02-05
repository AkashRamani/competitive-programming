#
# @lc app=leetcode id=421 lang=python3
#
# [421] Maximum XOR of Two Numbers in an Array
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.array = [None]*2

    def get_array_val(self,index):
        return self.array[index]
    def set_array(self, index, node):
        self.array[index] = node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_to_trie(self, number): #number is a 32 bit boolean string
        curr = self.root
        for bit in number:
            index = int(bit)
            if not curr.get_array_val(index):
                curr.set_array(index, TrieNode())
            curr = curr.get_array_val(index) #next

    def get_max_xor_from_array(self, number):
        curr = self.root

        xor = 0
        for bit in number:
            bit = int(bit)
            rev_bit = 1-bit

            if curr.get_array_val(rev_bit):
                xor = (xor<<1) | 1
                curr = curr.get_array_val(rev_bit)
            else:
                xor = xor << 1
                curr = curr.get_array_val(bit)
        return xor

    

class Solution:
    '''
       0 <= nums[i] <= 2^31-1, hence we can use 32 bit positive int.

        XOR with same number will be zero, so we will never get xor with self as our result, so no need to worry about that case
    '''

    def findMaximumXOR(self, nums: List[int]) -> int:

        def number_to_binary(number):
            return bin(number)[2:].zfill(32)
        
        #construct trie
        trie = Trie()

        for number in nums:
            trie.add_to_trie(number_to_binary(number))

        max_xor = 0
        for number in nums:
            max_xor = max(max_xor, trie.get_max_xor_from_array(number_to_binary(number)))

        return max_xor 

# @lc code=end

