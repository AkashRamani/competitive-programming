#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        hash_inorder = {}
        for index, val in enumerate(inorder):
            hash_inorder[val] = index

        def constructTree(preorder_start, preorder_end, inorder_start, inorder_end):
            if preorder_end - preorder_start <0:
                return None
            
            root = preorder[preorder_start]
            inorder_root_index = hash_inorder[root]

            len_left_sub_tree = inorder_root_index - inorder_start
            len_right_sub_tree = inorder_end - inorder_root_index

            left_sub_tree = constructTree(preorder_start+1, preorder_start+len_left_sub_tree, inorder_start, inorder_start + len_left_sub_tree -1)

            right_sub_tree = constructTree(preorder_start+len_left_sub_tree+1, preorder_start+len_left_sub_tree+len_right_sub_tree, inorder_root_index+1, inorder_root_index+len_right_sub_tree)

            return TreeNode(root,left_sub_tree ,right_sub_tree)

        return constructTree(0,len(preorder)-1, 0, len(inorder)-1)

 
# @lc code=end

