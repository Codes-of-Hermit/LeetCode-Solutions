class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        
        # dp[i][j] stores the Max ASCII Sum of the common subsequence 
        # between s1[:i] and s2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Check if characters match
                if s1[i-1] == s2[j-1]:
                    # Add current character's ASCII value to the diagonal result
                    dp[i][j] = dp[i-1][j-1] + ord(s1[i-1])
                else:
                    # Take the maximum of skipping a char from s1 vs s2
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Calculate total ASCII sum of both original strings
        total_ascii = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        
        # The answer is total sum minus the parts we kept (counted twice)
        return total_ascii - 2 * dp[m][n]