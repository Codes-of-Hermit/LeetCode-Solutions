class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        # 1. Coordinate Compression for X axis
        # Collect all x and x+l coordinates
        x_coords = set()
        for x, y, l in squares:
            x_coords.add(x)
            x_coords.add(x + l)
        
        # Sort unique x coordinates to form elementary intervals
        unique_x = sorted(list(x_coords))
        x_map = {val: i for i, val in enumerate(unique_x)}
        m = len(unique_x)
        
        # 2. Build Segment Tree arrays
        # The tree manages intervals between unique_x points. 
        # There are m-1 such intervals.
        # tree_cnt: tracks how many active squares cover a specific node range
        # tree_len: tracks the actual physical length covered by a node
        tree_size = 4 * m
        tree_cnt = [0] * tree_size
        tree_len = [0.0] * tree_size
        
        # Helper to update the segment tree
        def update(node, start, end, l_idx, r_idx, val):
            if l_idx >= r_idx:
                return

            if l_idx == start and r_idx == end:
                tree_cnt[node] += val
            else:
                mid = (start + end) // 2
                # Left child covers [start, mid]
                # Right child covers [mid, end]
                update(2 * node, start, mid, l_idx, min(r_idx, mid), val)
                update(2 * node + 1, mid, end, max(l_idx, mid), r_idx, val)
            
            # Recalculate length for this node
            if tree_cnt[node] > 0:
                # If this node is covered by at least one square, 
                # its active length is the full physical distance it represents.
                tree_len[node] = unique_x[end] - unique_x[start]
            else:
                # If not fully covered, it depends on children (if not leaf)
                if end - start == 1:
                    tree_len[node] = 0.0
                else:
                    tree_len[node] = tree_len[2 * node] + tree_len[2 * node + 1]

        # 3. Create Events (Y-axis sweep)
        # Event: (y, type, x_start, x_end)
        # Type 1 for bottom edge (add), -1 for top edge (remove)
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
        
        # Sort events by y coordinate
        events.sort()
        
        # 4. Sweep Line
        total_area = 0.0
        strips = [] # Store (y_height, active_width) to replay later
        
        prev_y = events[0][0]
        
        for y, type, x_start, x_end in events:
            # Calculate area added since the last event
            width = tree_len[1] # Root of segment tree has total active width
            height = y - prev_y
            
            if height > 0 and width > 0:
                area = width * height
                total_area += area
                strips.append((height, width, prev_y))
            
            # Update previous Y
            prev_y = y
            
            # Update Segment Tree
            # Map physical x coords to compressed indices
            l_idx = x_map[x_start]
            r_idx = x_map[x_end]
            update(1, 0, m - 1, l_idx, r_idx, type)
            
        # 5. Find the Split Point
        target = total_area / 2.0
        current_area = 0.0
        
        for height, width, start_y in strips:
            strip_area = width * height
            if current_area + strip_area >= target:
                # The target line is inside this strip
                needed = target - current_area
                # needed = width * (answer_y - start_y)
                return start_y + (needed / width)
            current_area += strip_area
            
        return float(prev_y) # Should theoretically not reach here