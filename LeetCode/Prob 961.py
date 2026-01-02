class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Set to store elements we have encountered so far
        seen = set()

        for num in nums:
            # If the number is already in the set, it's the one repeated N times
            if num in seen:
                return num
            # Otherwise, add it to the set and continue
            seen.add(num)
        
        return -1  # Should not be reached given problem constraints