#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time: O(n) and Space: O(1). 
        '''
        Floyd's Cycle Detection Algorithm: 
        - We use two pointers, fast and slow. fast moves 2x speed of slow
        - If there is a cycle, they will meet at some point.
            - why? because difference in relative speed is 1, so slow will cover the distance between them

        - If there is no cycle, hare will reach end of LL (None ptr).        
        '''
        hare = head
        tort = head

        while hare and hare.next:
            tort = tort.next
            hare = hare.next.next

            if hare == tort:
                return True
        return False




        ''' 
        Time: O(n) and Space: O(1)
        Had to use dummy head ^ avoided that in solution above (it is more clean)
        
        '''

        dummy = ListNode(0)
        dummy.next = head

        tort = dummy
        hare = head

        while hare and hare.next:
            if hare == tort:
                return True
            
            tort = tort.next
            hare = hare.next.next

        return False
# @lc code=end

