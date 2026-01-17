class Solution(object):
    def bestTower(self, towers, center, radius):
        """
        :type towers: List[List[int]]
        :type center: List[int]
        :type radius: int
        :rtype: List[int]
        """
        cx, cy = center
        max_quality = -1
        best_coordinate = [-1, -1]

        for x, y, q in towers:
            # 1. Calculate Manhattan Distance
            dist = abs(x - cx) + abs(y - cy)

            # 2. Check Reachability
            if dist <= radius:
                # 3. Check if this tower is better than the previous best
                
                # Priority 1: Higher Quality
                if q > max_quality:
                    max_quality = q
                    best_coordinate = [x, y]
                
                # Priority 2: Same Quality, Lexicographically Smaller Coordinate
                elif q == max_quality:
                    # In Python, list/tuple comparison handles lexicographical order automatically
                    # [x, y] < [best_x, best_y] checks x first, then y.
                    if [x, y] < best_coordinate:
                        best_coordinate = [x, y]

        return best_coordinate