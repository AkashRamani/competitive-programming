#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
            Tricky part here is maintaining a track of pointers..

            We iterate through the list.. as soon as we know a block is of size k
            We reverse the block and attach to tier opposite ends (this part is tricky to track)
            And proceed till we exausht the list

            Time: O(2*n) .., [we reverse k elements n/k times.. + n iterations]
            Space: O(k) = O(1)
        '''

        if k == 1:
            return head

        def twist_ll_and_attach(pre, head):
            tail = pre.next
            post = head.next

            prv = None
            current = tail
            while current != post:
                temp =  current.next

                current.next = prv
                prv = current
                current = temp
            pre.next = head
            tail.next = post

            return tail
            

        og_head = ListNode(0)
        og_head.next = head

        pre = og_head
        curr = head
        count = 0

        while curr:
            count+=1

            if count % k == 0:
                start = curr

                next_segment = curr.next

                pre = twist_ll_and_attach(pre, start)

                curr = next_segment

            else:
                curr = curr.next

        return og_head.next
        
# @lc code=end

