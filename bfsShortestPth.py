from collections import deque

def find_path_length(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    queue = deque([(start[0], start[1], 1)])  # (x, y, current path length)

    # Add 8-directional movements: (up, down, left, right, and diagonals)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  # Up, Down, Left, Right
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonals: Top-left, Top-right, Bottom-left, Bottom-right
    
    while queue:
        x, y, path_len = queue.popleft()
        
        # Check if we've reached the end point
        if (x, y) == end:
            return path_len
        
        # Explore all 8 possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, path_len + 1))
    
    return -1  # Return -1 if there is no path

# Example usage
matrix = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]
start = (0, 0)
end = (3, 3)

path_length = find_path_length(matrix, start, end)
print(path_length)  # Output: 5 (for example, it could take a diagonal shortcut to reduce path length)
