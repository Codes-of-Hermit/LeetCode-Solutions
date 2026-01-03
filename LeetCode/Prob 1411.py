class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Base case for n = 1
        # Type A: 3 colors (e.g., 123) -> 6 ways
        # Type B: 2 colors (e.g., 121) -> 6 ways
        type_a = 6
        type_b = 6
        
        # Iterate from the 2nd row up to n
        for i in range(2, n + 1):
            # Calculate new values based on the formulas derived
            new_type_a = (2 * type_a + 2 * type_b) % MOD
            new_type_b = (2 * type_a + 3 * type_b) % MOD
            
            # Update current state
            type_a = new_type_a
            type_b = new_type_b
            
        return (type_a + type_b) % MOD