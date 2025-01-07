#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        '''
            Implemented bfs using a queue.. usingppython collection's deque Data struct..

            queue stores the node along withits level from the root (root being 0)
            and we first append and then go to next (because we want in-order-traversal)

            Time: O(n)
            Space: O(n)

            bilblography: dfs can run into infitine depth problem... but BFS cant.. BFS uses a lot more memory in-general.
                            DFS with increasing depths is an algo that can tackle the drawbacks of normal DFS (without going into infinite depth problems)
                            Used in Ai realted algos.. like A*


        ''' 
        if not root:
            return []

        queue = deque([(root, 0)])
        ans = []
        while queue:
            node, level = queue.popleft()

            if not node:
                continue

            if level > len(ans)-1:
                ans.append([])
            ans[level].append(node.val)

            if node.left:
                queue.append((node.left, level+1))
            
            if node.right:
                queue.append((node.right, level+1))
            
        return ans
            

# @lc code=end

