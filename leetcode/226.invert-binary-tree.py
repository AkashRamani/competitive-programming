#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
            DFS.. and invert as you reach the depths..
            Time: O(n) .. n being #nodes in tree
            Space: O(n) .. 
                why? since dfs.. we will have a stack of size h (height of tree)
                since this is not necesarily a balanced binary tree.. worst case height can be O(n).

        '''
        if not root:
            return None

        right = self.invertTree(root.right)
        left =  self.invertTree(root.left)

        root.left = right
        root.right = left
        return root
# @lc code=end

