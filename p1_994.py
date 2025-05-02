# 994. Rotting Oranges

# TC : O(m × n) where m is the number of rows and n is the number of columns in the grid. We visit each cell at most once.
# SC : O(m × n) for the queue in the worst case, where all oranges are rotten initially.

# Did this code successfully run on Leetcode : yes

# Approach :
# Handle edge cases: if the grid is empty, return 0.
# Get the dimensions of the grid.
# Initialize a queue for BFS and a counter for fresh oranges.
# Traverse the grid to:
    # Add all initially rotten oranges to the queue with their positions and minute count (0).
    # Count all fresh oranges.
# If there are no fresh oranges initially, return 0 (no time needed).
# Perform BFS:
    # Pop a rotten orange from the queue.
    # Check all four adjacent cells (up, down, left, right).
    # If an adjacent cell contains a fresh orange, rot it, decrease the fresh orange count, and add it to the queue with an incremented minute count.
    # Keep track of the maximum minute count seen.
# After BFS, if there are still fresh oranges, return -1 (impossible to rot all oranges).
# Otherwise, return the maximum minute count, which is the minimum time needed for all oranges to rot.
# This solution efficiently simulates the rotting process by using BFS to rot oranges level by level, where each level represents one minute of elapsed time.

from collections import deque
from typing import Collection, List, Optional

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        # Get grid dimensions
        rows, cols = len(grid), len(grid[0])
        
        # Initialize queue with all rotten oranges
        queue = []
        fresh_count = 0
        
        # Count fresh oranges and add rotten oranges to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, minutes)
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # If there are no fresh oranges, return 0
        if fresh_count == 0:
            return 0
        
        # Perform BFS to rot oranges
        max_minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right
        
        while queue:
            row, col, minutes = queue.pop(0)
            max_minutes = max(max_minutes, minutes)
            
            # Check all 4 adjacent cells
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if valid cell with fresh orange
                if (0 <= new_row < rows and 0 <= new_col < cols and 
                    grid[new_row][new_col] == 1):
                    # Rot the orange
                    grid[new_row][new_col] = 2
                    fresh_count -= 1
                    # Add to queue with increased time
                    queue.append((new_row, new_col, minutes + 1))
        
        # If there are still fresh oranges, it's impossible
        if fresh_count > 0:
            return -1
        
        return max_minutes
        