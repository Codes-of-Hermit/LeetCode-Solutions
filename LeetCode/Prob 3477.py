class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(fruits)
        # Keep track of which baskets are already used
        occupied = [False] * n
        
        unplaced_count = 0
        
        # Iterate through each fruit we need to place
        for fruit_qty in fruits:
            placed = False
            
            # Check baskets from left to right
            for j in range(n):
                # We need a basket that is NOT occupied AND has enough capacity
                if not occupied[j] and baskets[j] >= fruit_qty:
                    occupied[j] = True # Mark as used
                    placed = True      # Mark fruit as successfully placed
                    break              # Stop looking for a basket for this fruit
            
            # If the loop finished and we didn't place the fruit, count it
            if not placed:
                unplaced_count += 1
                
        return unplaced_count