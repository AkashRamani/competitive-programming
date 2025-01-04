#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        ''' 
            | left_height - right_height | <= 1   ∀ nodes
            
            Time Space: O(n) ~ O(h) .. if I use the second approach that sort of does an early return 
                                        and hence it is always like traversing a balanced binary tree. O(h) = O(log n)
        '''
        # self.is_balanced = True

        # def dfs_depth(root):
        #     if not root:
        #         return 0

        #     left_height = dfs_depth(root.left) 
        #     right_height = dfs_depth(root.right)

        #     if abs(left_height - right_height) > 1:
        #         # return False
        #         self.is_balanced = False
            
        #     return 1+ max(left_height, right_height)

        # dfs_depth(root)
        # return self.is_balanced

        '''
            This is much better.. -1 propogates outwards.. if returned value is -1 that means Not balanced
        '''

        def dfs_depth(root):
            if not root:
                return 0

            left_height = dfs_depth(root.left) 
            if left_height == -1:
                return -1

            right_height = dfs_depth(root.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1
            
            return 1+ max(left_height, right_height)

        return dfs_depth(root) != -1

            
        
# @lc code=end

