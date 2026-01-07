# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # List to store the sum of every subtree we encounter
        all_subtree_sums = []
        
        # Helper DFS function to calculate sum of current subtree
        def subtree_sum(node):
            if not node:
                return 0
            
            # Recursive step: Sum = Node + Left_Sum + Right_Sum
            current_sum = node.val + subtree_sum(node.left) + subtree_sum(node.right)
            
            # Store this sum for later comparison
            all_subtree_sums.append(current_sum)
            
            return current_sum
        
        # 1. Calculate sums of all subtrees
        # The sum of the root (the last value calculated) is the Total Sum
        total_sum = subtree_sum(root)
        
        max_product = 0
        
        # 2. Iterate through every subtree sum to find the max product
        for s in all_subtree_sums:
            # Formula: Part1 * Part2
            # Part1 = s
            # Part2 = total_sum - s
            current_product = s * (total_sum - s)
            max_product = max(max_product, current_product)
            
        # Return result modulo 10^9 + 7
        return max_product % (10**9 + 7)