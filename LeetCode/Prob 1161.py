# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        # Initialize variables
        max_sum = float('-inf')  # Start very low to handle negative sums
        ans_level = 1            # The level with the max sum
        current_level = 1
        
        # Queue for BFS, starting with root
        queue = collections.deque([root])
        
        while queue:
            level_sum = 0
            level_size = len(queue)
            
            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                # Add children to queue for next level processing
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Check if this level has a higher sum than what we've seen
            if level_sum > max_sum:
                max_sum = level_sum
                ans_level = current_level
            
            # Move to the next level
            current_level += 1
            
        return ans_level