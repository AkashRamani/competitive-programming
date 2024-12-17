#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        while n:
            curr = curr.next
            n=n-1
        
        prv = dummy
        while curr:
            curr = curr.next
            prv = prv.next
        
        prv.next = prv.next.next
        
        return dummy.next
        
# @lc code=end

