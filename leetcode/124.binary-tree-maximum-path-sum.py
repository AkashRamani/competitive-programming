#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_sum = float("-inf")

        def dfs_max_path_sum(node):
            if not node:
                return 0

            left_sub_tree_max = max(dfs_max_path_sum(node.left), 0) #This does the trick, since we want a maximal path... if subtree pathsum turns out to be -ve.. no point in adding a value...
            right_sub_tree_max = max(dfs_max_path_sum(node.right), 0)


            self.max_sum = max(self.max_sum, left_sub_tree_max + node.val +right_sub_tree_max )

            return max(left_sub_tree_max ,right_sub_tree_max) + node.val

        dfs_max_path_sum(root)
        return self.max_sum


        # And if you are a rebel and dont want to use max(dfs, 0)..

        self.max_sum = float("-inf")

        def dfs_max_path_sum(node):
            if not node:
                return 0

            left_sub_tree_max = dfs_max_path_sum(node.left)
            right_sub_tree_max = dfs_max_path_sum(node.right)


            self.max_sum = max(self.max_sum, node.val, left_sub_tree_max + node.val, node.val +right_sub_tree_max, left_sub_tree_max + node.val +right_sub_tree_max )

            return max(left_sub_tree_max ,right_sub_tree_max, 0) + node.val

        dfs_max_path_sum(root)
        return self.max_sum

# @lc code=end

