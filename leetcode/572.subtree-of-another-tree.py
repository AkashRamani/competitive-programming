#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        '''
            NOTE -- never forget to make the scope global when using a varaible withing a recursive function

            BRUTE..
            Idea is traverse a tree (I am doing dfs )and if a node with same value as subRoot is found run a DFS to check if matching tree with main trees node as node1
            Time: O(n * k) => n is nodes in main tree, n -> size(main-tree), k -> size(sub-tree) 
            Space: O (n+k)



            2 traversal string and check sub-string does not work too.. it has a flaw [in 1st order a sub strng may match, but in 2nd it might not be the same subtrees]

            https://leetcode.com/problems/subtree-of-another-tree/editorial/

            TAKE-AWAY: It is possible to uniquely identify a single subtree using a single traversal order.. if we include # for Null values.
            Once we have both traversal orders it is simply a problem of checking is substr1 in subtr2
        '''
        def is_same_tree(node1, node2):
            global is_subtree
            if bool(node1) ^ bool(node2):
                return False
            if node1 and node2 and node1.val != node2.val:
                return False
            if not node1:
                return True
            
            return is_same_tree(node1.left, node2.left) and is_same_tree(node1.right, node2.right)


        def dfs(node,subRoot):
            if not node:
                return False

            if is_same_tree(node, subRoot): #is_same_tree function makes an early return so no need to checkif a matching values.. dsnt rly affect time
                return True

            return dfs(node.left, subRoot) or dfs(node.right, subRoot)
            
        return dfs(root, subRoot)




        '''
            Brute force, this makes an early return..
        '''
        # is_subtree = False

        # def is_same_tree(node1, node2):
        #     if bool(node1) ^ bool(node2):
        #         return False
        #     if node1 and node2 and node1.val != node2.val:
        #         return False
        #     if not node1:
        #         return True
            
        #     return is_same_tree(node1.left, node2.left) and is_same_tree(node1.right, node2.right)


        # def dfs(node,subRoot):
        #     if not node:
        #         return

        #     if is_same_tree(node, subRoot):
        #         return -1

        #     if dfs(node.left, subRoot) == -1:
        #         return -1
        #     if dfs(node.right, subRoot) == -1:
        #         return -1
        
        # return dfs(root, subRoot) == -1     
# @lc code=end

