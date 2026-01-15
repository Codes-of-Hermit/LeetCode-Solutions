class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """
        # Helper function to find the max consecutive bars
        def get_max_gap(bars):
            if not bars:
                return 1
            
            bars.sort()
            max_consecutive = 1
            current_consecutive = 1
            
            for i in range(1, len(bars)):
                # If current bar is exactly 1 greater than previous, it's consecutive
                if bars[i] == bars[i-1] + 1:
                    current_consecutive += 1
                else:
                    # Sequence broken, reset count
                    current_consecutive = 1
                
                # Update the maximum found so far
                max_consecutive = max(max_consecutive, current_consecutive)
            
            # The gap size is always consecutive bars + 1
            return max_consecutive + 1

        # 1. Calculate max continuous gap for height and width
        max_h_gap = get_max_gap(hBars)
        max_v_gap = get_max_gap(vBars)
        
        # 2. The side of the square is limited by the smaller gap
        side = min(max_h_gap, max_v_gap)
        
        # 3. Return Area
        return side * side