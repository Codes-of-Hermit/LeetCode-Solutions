class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store value -> index
        seen = {}
        
        # Iterate through the list with both index (i) and value (num)
        for i, num in enumerate(nums):
            
            # Calculate what number we need to find
            complement = target - num
            
            # If we have seen the complement before, we are done!
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, store the current number and index for future checks
            seen[num] = i
            
        return [] # Should not happen based on problem constraints