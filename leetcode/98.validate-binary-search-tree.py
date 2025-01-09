#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
            Intution..
            root is always valid (lower bound = -inf and upper bound = inf)
                when I move left..   (lower bound = -inf and upper bound = root)
                when I move right..  (upper bound = root and upper bound = inf)

        '''

        def dfs_valid_bst(node, lower_bound, upper_bound):
            if not node:
                return True
            
            if not (lower_bound < node.val < upper_bound):
                return False
            
            return dfs_valid_bst(node.left, lower_bound, node.val) and dfs_valid_bst(node.right, node.val, upper_bound)

        return dfs_valid_bst(root, float('-inf'), float('inf'))
             

        '''
            At every node check if left node is less and right greater than parent...

            This approach will give this tree as True;;  but this is not becase 3 CANNOT be on the right-subtree of 5.
                    5
                   / \
                  4   6
                     / \
                    3   7 

            So we will need to propogate runningMin an runningMax, and use that to compare. Correct approach above

        '''
        #NOTEEEEE -- this is incorrect version (^ read)        
        self.flag = True

        def dfs(node):
            if not node:
                return True
            
            dfs(node.left)

            l = True
            if node.left is not None and node.left.val >= node.val:
                l = False
                self.flag = False

            
            dfs(node.right)
            r = True
            if node.right is not None and node.right.val <= node.val:
                
                r = False
                self.flag = False
            return self.flag and l and r

        return dfs(root)

               
        
# @lc code=end

