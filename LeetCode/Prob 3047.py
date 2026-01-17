class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """
        n = len(bottomLeft)
        max_side = 0
        
        # Iterate through every unique pair of rectangles
        for i in range(n):
            # Extract coordinates for rect 1
            ax1, ay1 = bottomLeft[i]
            ax2, ay2 = topRight[i]
            
            for j in range(i + 1, n):
                # Extract coordinates for rect 2
                bx1, by1 = bottomLeft[j]
                bx2, by2 = topRight[j]
                
                # Calculate Intersection Boundaries
                # Logic: The intersection is the max of the lefts and min of the rights
                inter_x1 = max(ax1, bx1)
                inter_x2 = min(ax2, bx2)
                
                # Logic: The intersection is the max of the bottoms and min of the tops
                inter_y1 = max(ay1, by1)
                inter_y2 = min(ay2, by2)
                
                # Check if there is a valid overlap (width > 0 and height > 0)
                if inter_x2 > inter_x1 and inter_y2 > inter_y1:
                    width = inter_x2 - inter_x1
                    height = inter_y2 - inter_y1
                    
                    # The largest square we can fit is limited by the shorter dimension
                    current_square_side = min(width, height)
                    
                    if current_square_side > max_side:
                        max_side = current_square_side
                        
        # Return area
        return max_side * max_side