class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        
        for n in nums:
            if n % 2 == 0:
                # Even numbers cannot be formed by x | (x + 1)
                result.append(-1)
            else:
                # Find the position of the first '0' bit starting from LSB
                # Example: n = 11 (binary 1011)
                # Bit 0 is 1
                # Bit 1 is 1
                # Bit 2 is 0 -> Stop here. The sequence of trailing 1s is bits 0-1.
                # To minimize x, we remove the highest bit in that sequence (Bit 1).
                
                # We can find the lowest zero bit using a trick or a simple loop.
                # Since numbers are small (< 1000), a loop is very fast.
                for i in range(31):
                    if not ((n >> i) & 1):
                        # Found the first zero at position i.
                        # The bit to flip is i - 1.
                        result.append(n - (1 << (i - 1)))
                        break
                        
        return result