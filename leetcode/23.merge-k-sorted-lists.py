#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
            Time: O(n * logk)
            Space: O(1).. merging two lists was in place( ∵ we used existing nodes of the two lists) & aggregated in the same list(∵ we maintained a variable l)

            Merge sort ke merge array jaisa..

            merging two arrays take O(n) time.. <n being the len of largest list among all k>
            we have k arrays, had we clubbed first-two, then with third, forth, ... It would take us k steps to combine all ==> O(k.n)

            But if we do 1st two, next two and so on.. it will take us O((log k) * n)
        '''

        if not lists:
            return None

        def merge_two_lists(L1: List, L2:List):
            head = ListNode(0)
            curr = head

            while L1 and L2:
                if L1.val < L2.val:
                    curr.next = L1
                    L1 = L1.next
                else:
                    curr.next = L2
                    L2 = L2.next
                curr = curr.next

            if L1:
                curr.next = L1
            elif L2:
                curr.next = L2
            return head.next

        l = len(lists)

        while l > 1:
            for i in range(0, l, 2):
                L1 = lists[i]
                L2 = lists[i+1] if i+1<l else None

                #Merge two lists
                L = merge_two_lists(L1, L2)

                lists[i//2] = L

            l = (l+1)//2

        return lists[0]
# @lc code=end

