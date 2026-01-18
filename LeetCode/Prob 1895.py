class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        # Precompute Prefix Sums for Rows and Cols
        # row_prefix[i][j] = sum of grid[i][0]...grid[i][j-1]
        row_prefix = [[0] * (n + 1) for _ in range(m)]
        # col_prefix[i][j] = sum of grid[0][j]...grid[i-1][j]
        col_prefix = [[0] * n for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                row_prefix[i][j+1] = row_prefix[i][j] + grid[i][j]
                col_prefix[i+1][j] = col_prefix[i][j] + grid[i][j]
                
        # Helper to check if a specific kxk square at (r, c) is magic
        def is_magic(r, c, k):
            # 1. Get the target sum from the first row
            # Sum of row r from col c to c+k
            target = row_prefix[r][c+k] - row_prefix[r][c]
            
            # 2. Check all rows
            for i in range(k):
                current_row_sum = row_prefix[r+i][c+k] - row_prefix[r+i][c]
                if current_row_sum != target:
                    return False
            
            # 3. Check all columns
            for j in range(k):
                current_col_sum = col_prefix[r+k][c+j] - col_prefix[r][c+j]
                if current_col_sum != target:
                    return False
            
            # 4. Check Diagonals
            # Main diagonal
            d1 = 0
            for i in range(k):
                d1 += grid[r+i][c+i]
            if d1 != target:
                return False
                
            # Anti-diagonal
            d2 = 0
            for i in range(k):
                d2 += grid[r+i][c+k-1-i]
            if d2 != target:
                return False
                
            return True

        # Iterate size k from max possible down to 2
        for k in range(min(m, n), 1, -1):
            # Iterate through all top-left positions valid for size k
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
                        
        return 1