#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        """
        Time :O(n) ; Space O(1) --> No new nodes are created, we simply manipulated the references

        Do not return anything, modify head in-place instead.

            Divide the list in half
            reverse the latter half
            
            merge both lists, element by element

            Reas in-line comments only if you dont undertand the code
        """

        i, j = head, head

        # slow ptr, fast ptr to get i at pos[mid+1]. lways len(l1)> len(l2)
        while j and j.next:
            i = i.next
            j=j.next.next

        # starting from i.next till end of list; reverse list.
        # Also dont forget to point i.next to Null;  signifying end of Fist List
        prv = None
        curr = i.next
        i.next = None 
        while curr:
            temp = curr.next
            curr.next = prv

            prv = curr
            curr = temp
        head2 = prv #head of reverse latter half

        head1 = head #head of first array

        #merge them in-place within list2
        while head1 and head2:
            temp1 = head1.next

            head1.next = head2
            head2 = head2.next

            head1.next.next = temp1
            head1 = temp1

        #As question suggests, return nothing!
 
# @lc code=end

