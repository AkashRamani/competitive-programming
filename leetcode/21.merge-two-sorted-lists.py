#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
            Time: O(max(m,n)) or m+n 
            Spcae: O(1) ==> becuase we simply reassign node references
        '''

        L1 = list1
        L2 = list2

        L3 = ListNode()
        head = L3

        while L1 and L2:
            if L1.val > L2.val:
                L3.next = L2
                L2 = L2.next
            else:
                L3.next = L1
                L1 = L1.next

            L3 = L3.next
        
        if L1:
            L3.next = L1

        if L2:
            L3.next = L2

        return head.next
# @lc code=end

