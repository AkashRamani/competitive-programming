#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs_is_same(root1, root2):
            if bool(root1) ^ bool(root2): #any one is null
                return False

            if root1 and root2:
                if root1.val != root2.val:
                    return False

            if not root1: #this means r1 and r2 both are null
                return True
                
            return dfs_is_same(root1.left, root2.left) and dfs_is_same(root1.right, root2.right)
        return dfs_is_same(p, q)

        '''
            Implement using bfs next
        '''


# @lc code=end

