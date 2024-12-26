#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
            Time: O(n)
            Space: O(n)

            tried doing it by maintaining a single curr and not using any extra space, but that code becomes very tedious
        '''
        head = ListNode(0)
        curr = head
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            add = v1+v2+carry
            carry = add//10
            digit = add % 10

            new_node = ListNode(digit, None)
            curr.next = new_node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next
        return head.next
# @lc code=end

