#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        '''
            time and space: O(n)
        '''

        self.max_diameter = 0

        def dfs_diameter(root):
            nonlocal max_diameter
            if not root:
                return 0
            
            left_height = dfs_diameter(root.left)
            right_height = dfs_diameter(root.right)

            self.max_diameter = max(self.max_diameter, left_height + right_height)

            return 1+max(left_height,right_height)
                
        dfs_diameter(root)
        return self.max_diameter
        


        '''
            I dont like the use of non-local variable..
            1. You can somehow include it within the scope/encapulate (diameter+the function) in a class
            2. use self.max_diametere .. which sort of replicates point1 in python?
            3. make the function return 2 variables, max_depth and max_diameter .. not a fan of this
        '''
        max_diameter = 0

        def dfs_diameter(root):
            nonlocal max_diameter
            if not root:
                return 0
            
            left_height = dfs_diameter(root.left)
            right_height = dfs_diameter(root.right)

            max_diameter = max(max_diameter, left_height + right_height)

            return 1+max(left_height,right_height)
                
        dfs_diameter(root)
        return max_diameter
        
        
# @lc code=end

