class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
            
        rows = len(matrix)
        cols = len(matrix[0])
        
        # This array will hold the "height" of 1s for the current row
        heights = [0] * cols
        max_area = 0
        
        for r in range(rows):
            # 1. Update the histogram heights for this row
            for c in range(cols):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0
            
            # 2. Calculate max area for the current histogram state
            current_area = self.largestRectangleArea(heights)
            max_area = max(max_area, current_area)
            
        return max_area

    def largestRectangleArea(self, heights):
        """
        Helper function: Finds the largest rectangle in a histogram 
        using a Monotonic Stack.
        """
        stack = [-1]  # Stack stores indices. -1 is a dummy index for left boundary
        max_h_area = 0
        
        # Append a 0 height at the end to force processing remaining bars in stack
        for i, h in enumerate(heights + [0]):
            # While the current bar is shorter than the bar at stack top,
            # we found the right boundary for the bar at stack top.
            while stack[-1] != -1 and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_h_area = max(max_h_area, height * width)
            
            stack.append(i)
            
        return max_h_area