#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        '''
            DFS that traverses right depth first.
            If at a level no values exists append else dont
        '''
        level_array = []
        def dfs(node, level):
            if not node:
                return
            if level > len(level_array)-1:
                level_array.append(node.val)

            dfs(node.right, level+1)
            dfs(node.left, level+1)

        dfs(root, 0)
        return level_array

        '''
            Iteratively: coding the same approach.. need to use stack for DFS
        '''
        if not root:
            return []
        stack = deque([(root, 0)])
        level_array = []

        while stack:
            node, level = stack.pop()

            if not node:
                continue
            
            if level > len(level_array)-1:
                level_array.append(node.val)
            
            stack.append((node.left, level+1))
            stack.append((node.right, level+1)) # because we want to pop right first 
            
        return level_array
# @lc code=end

