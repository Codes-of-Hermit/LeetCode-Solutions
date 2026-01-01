class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Get the length of the list
        n = len(digits)
        
        # 1. Iterate backwards from the last digit to the first
        # range(start, stop, step) -> start at last index, go down to -1 (exclusive)
        for i in range(n - 1, -1, -1):
            
            # Case A: The digit is less than 9 (e.g., 1, 2, ... 8)
            if digits[i] < 9:
                digits[i] += 1
                # We found a spot to add 1 without a carry, so we are done.
                return digits
            
            # Case B: The digit is 9
            # It becomes 0, and the loop continues to carry the 1 to the next left digit
            digits[i] = 0
            
        # Case C: If the loop finishes, it means all digits were 9s (e.g., 99 -> 00)
        # We need to add the leading 1.
        return [1] + digits