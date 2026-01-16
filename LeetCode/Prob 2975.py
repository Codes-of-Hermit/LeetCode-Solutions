class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """
        # 1. Add boundaries to the fence lists and sort them
        hFences.extend([1, m])
        vFences.extend([1, n])
        
        hFences.sort()
        vFences.sort()
        
        # 2. Collect all possible vertical gaps (heights)
        h_gaps = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_gaps.add(hFences[j] - hFences[i])
        
        # 3. Collect all possible horizontal gaps (widths)
        # However, to save time/space, we can check for intersection on the fly,
        # or just build a second set and intersect. 
        # Given N <= 600, building two sets is perfectly fast.
        v_gaps = set()
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                v_gaps.add(vFences[j] - vFences[i])
        
        # 4. Find the intersection of possible heights and widths
        common_gaps = h_gaps.intersection(v_gaps)
        
        if not common_gaps:
            return -1
            
        # 5. Get the largest side and calculate area
        max_side = max(common_gaps)
        mod = 10**9 + 7
        
        return (max_side * max_side) % mod