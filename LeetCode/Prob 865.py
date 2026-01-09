# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Helper function returns a pair: (height, lca_node)
        def dfs(node):
            if not node:
                return 0, None
            
            # Post-order traversal: process children first
            left_height, left_lca = dfs(node.left)
            right_height, right_lca = dfs(node.right)
            
            # Case 1: Both sides are equally deep
            # The current node is the common ancestor
            if left_height == right_height:
                return left_height + 1, node
            
            # Case 2: Left side is deeper
            # The answer is whatever the left side found
            elif left_height > right_height:
                return left_height + 1, left_lca
            
            # Case 3: Right side is deeper
            # The answer is whatever the right side found
            else:
                return right_height + 1, right_lca
        
        # We only care about the node part of the result
        return dfs(root)[1]