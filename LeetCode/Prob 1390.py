class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        
        for num in nums:
            # Skip 0 or very small numbers early if needed, 
            # though the logic handles them naturally.
            
            divisor_count = 0
            divisor_sum = 0
            
            # Iterate from 1 up to integer square root of num
            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:
                    # Found a divisor pair (i, num/i)
                    
                    if i * i == num:
                        # Perfect square (e.g., 4 -> 2*2), count only one divisor
                        divisor_count += 1
                        divisor_sum += i
                    else:
                        # Distinct pair (e.g., 21 -> 3*7), count both
                        divisor_count += 2
                        divisor_sum += i + (num // i)
                
                # Optimization: If we already exceed 4 divisors, stop checking this number
                if divisor_count > 4:
                    break
            
            # If exactly 4 divisors were found, add their sum to the answer
            if divisor_count == 4:
                total_sum += divisor_sum
                
        return total_sum