#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        '''
            since smallest.. dfs and traverse left first, after each node decrement k

            for a node..
                we look left, decrease k.. look at node.. loook right
                
        '''

        self.k = k
        self.answer = None

        def dfs(node):
            if not node:
                return 
            if self.k == 0:
                self.answer = node.val

            
            dfs(node.left)
            self.k = self.k-1
            if self.k == 0:
                self.answer = node.val
                return

            dfs(node.right)

        dfs(root)
        return self.answer
# @lc code=end

