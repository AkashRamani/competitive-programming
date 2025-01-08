#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        queue = deque([(root, float('-inf'))])
        count_of_good_nodes = 0

        while queue:
            node, max_val = queue.popleft()

            if not node:
                continue
            
            if node.val >= max_val:
                max_val = node.val
                count_of_good_nodes+=1
            
            queue.append((node.left, max_val))
            queue.append((node.right, max_val))

        return count_of_good_nodes



        # def dfs(node, max_val):
        #     if not node:
        #         return 0

        #     counter = 0
        #     if node.val >= max_val:
        #         max_val = node.val
        #         counter = 1
    
        #     return counter + dfs(node.left, max_val) + dfs(node.right, max_val)

        # return dfs(root, float('-inf'))


'''
    LOVE THISSSS
'''

class Solution2:
    def __init__(self):
        self.nodeList = list()

    def findGoodNodes(self, root, maxForPath):
        if root.val >= maxForPath:
            self.nodeList.append(root.val)
            if root.val > maxForPath:
                maxForPath= root.val
        if root.left:
            self.findGoodNodes(root.left, maxForPath)
        if root.right:
            self.findGoodNodes(root.right, maxForPath)
    def goodNodes(self, root: TreeNode) -> int:
        if root:
            self.findGoodNodes(root, root.val)
        return len(self.nodeList)

# @lc code=end

