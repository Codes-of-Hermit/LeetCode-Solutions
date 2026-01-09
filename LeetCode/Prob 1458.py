class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        m = len(nums2)
        
        # Initialize DP table with a very small number
        # dp[i][j] stores the max dot product for nums1[0...i] and nums2[0...j]
        dp = [[float('-inf')] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                # Calculate product of current pair
                product = nums1[i] * nums2[j]
                
                # Option 1: Start fresh with this product
                # Option 2: Add to previous best diagonal (if valid)
                if i > 0 and j > 0:
                    dp[i][j] = max(product, dp[i-1][j-1] + product)
                else:
                    dp[i][j] = product
                
                # Option 3 & 4: Carry over best results from skipping elements
                # (Check previous row)
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                # (Check previous col)
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1])
                    
        # The bottom-right corner contains the result for the full arrays
        return dp[n-1][m-1]