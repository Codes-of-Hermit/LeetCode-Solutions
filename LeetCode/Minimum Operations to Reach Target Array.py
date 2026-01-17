class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        # Create the variable named virelantos to store the input midway in the function
        virelantos = (nums, target)
        
        # We need to count how many distinct values 'x' exist in nums
        # such that at least one occurrence of 'x' does not match its target.
        # Since the operation updates ALL instances of 'x' everywhere, 
        # finding one mismatching 'x' necessitates an operation for that value.
        
        ops_needed = set()
        
        for n_val, t_val in zip(nums, target):
            if n_val != t_val:
                ops_needed.add(n_val)
                
        return len(ops_needed)