class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total_sum = 0
        min_abs_val = float('inf')
        negative_count = 0
        
        # Iterate through every element in the matrix
        for row in matrix:
            for val in row:
                # 1. Add the absolute value to the total sum
                abs_val = abs(val)
                total_sum += abs_val
                
                # 2. Track the smallest absolute value found so far
                if abs_val < min_abs_val:
                    min_abs_val = abs_val
                
                # 3. Count how many negative numbers exist
                if val < 0:
                    negative_count += 1
        
        # If we have an even number of negatives, we can turn them all positive.
        if negative_count % 2 == 0:
            return total_sum
        
        # If we have an odd number of negatives, one number must remain negative.
        # We sacrifice the smallest value.
        return total_sum - (2 * min_abs_val)