from collections import deque

def find_path_length(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    queue = deque([(start[0], start[1], 1)])  

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  # Up, Down, Left, Right
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonals: Top-left, Top-right, Bottom-left, Bottom-right
    
    while queue:
        x, y, path_len = queue.popleft()
        
        if (x, y) == end:
            return path_len
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, path_len + 1))
    
    return -1 

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
