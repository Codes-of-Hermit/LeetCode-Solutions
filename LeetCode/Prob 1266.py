class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total_time = 0
        
        # Iterate from the first point up to the second-to-last point
        for i in range(len(points) - 1):
            curr_point = points[i]
            next_point = points[i+1]
            
            # Calculate absolute differences in X and Y
            delta_x = abs(curr_point[0] - next_point[0])
            delta_y = abs(curr_point[1] - next_point[1])
            
            # The time to travel between two points is the max of the differences
            # (because diagonal moves cover 1 unit of X and 1 unit of Y simultaneously)
            total_time += max(delta_x, delta_y)
            
        return total_time