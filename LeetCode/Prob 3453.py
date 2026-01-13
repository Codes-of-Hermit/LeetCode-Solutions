class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        # 1. Calculate boundaries and Total Area
        total_area = 0
        min_y = float('inf')
        max_y = float('-inf')
        
        for x, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)
            
        target = total_area / 2.0
        
        # 2. Binary Search
        # We perform a fixed number of iterations to handle floating point precision.
        # 70 iterations is enough to reduce the error range to negligible for 10^9 inputs.
        low = min_y
        high = max_y
        
        for _ in range(70):
            mid = (low + high) / 2.0
            current_area = 0
            
            # Calculate area below the 'mid' line
            for x, y, l in squares:
                # Square Top Edge
                sq_top = y + l
                
                if mid <= y:
                    # Line is below the square - 0 contribution
                    continue
                elif mid >= sq_top:
                    # Line is above the square - full contribution
                    current_area += l * l
                else:
                    # Line cuts through the square
                    # Height of the bottom portion is (mid - y)
                    # Width is l
                    current_area += l * (mid - y)
            
            # Binary Search Logic
            if current_area < target:
                # Not enough area yet, move line up
                low = mid
            else:
                # Enough area (or gap plateau), try to find a lower line
                high = mid
                
        return high