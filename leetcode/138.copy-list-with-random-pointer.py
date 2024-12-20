#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
            Time and Space : O(n)
        '''

        curr = head

        new_head = Node(0)
        new = new_head #new 
        old_to_new_map = {}

        #copy LL - w/o random
        while curr:
            new_node = Node(curr.val, None, None) 
            old_to_new_map[curr] = new_node
            
            new.next = new_node

            new = new.next
            curr = curr.next

        new_head = new_head.next #start mein we added a dummy node


        #2nd iteration, we resolve random pointer for the new LL
        curr_old = head
        curr_new = new_head
        while curr_old:
            curr_new.random = old_to_new_map.get(curr_old.random, None)

            curr_old = curr_old.next
            curr_new = curr_new.next

        return new_head
# @lc code=end

