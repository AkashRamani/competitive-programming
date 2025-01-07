#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        '''
         Since binary search tree and we cut search space.. 
         O(height) ~ O(log n)


         This approach does not check with p or q.. it simply chcks where there a split.. 
         and leverages the fact that a solution is guranteeed to exist
        '''

        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

        '''
            O(n) ... dfs and when a node== p or q, we return a node instead of 1
        '''
        def dfs(node):
            # Base case: if the node is None, return None
            if not node:
                return None
            
            # If the current node is either p or q, return the node
            if node == p or node == q:
                return node
            
            # Recursively search in the left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If both left and right subtrees return a node, the current node is the LCA
            if left and right:
                return node
            
            # If only one subtree returns a node, return that node
            return left or right

        # Start DFS from the root
        return dfs(root)


        '''
            My approach tath didnt work.
        
        '''
        self.answer_node = None
        def dfs(node, p, q):
            if not node:
                return 0
            
            if not self.answer_node and dfs(node.left, p, q) + dfs(node.right, p, q) == 2:
                self.answer_node = node
                return 2

            if node.val in [p.val, q.val]:
                return 1
            else:
                return 0
        dfs(root, p, q)
        return self.answer_node

    
# @lc code=end

