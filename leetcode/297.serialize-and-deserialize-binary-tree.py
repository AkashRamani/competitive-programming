#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        '''
            LEVERAGING FACT THAT:  Dfs/bfs with Null Nodes recorded is suffiecnt to construct back a Binary Tree.. 
            reference - https://leetcode.com/problems/subtree-of-another-tree/editorial/

            So computing DFS with in-order trav.. because its easiest to construct a tree coz, first node is root
        '''
        self.array = []
        def dfs(node):
            if not node:
                self.array.append('N')
                return

            self.array.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(self.array)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        '''
            using a self.index {class varibale works} too
        '''

        def constructTree(index = 0):
            if index >= len(self.array):
                return None, index
            
            root_val = self.array[index]
            if root_val== 'N':
                return None, index+1

            left_node, index = constructTree(index+1)
            right_node, index = constructTree(index)

            return TreeNode(int(root_val), left_node, right_node), index
        
    
        self.array = data.split(',')
        root, _ = constructTree(0)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

