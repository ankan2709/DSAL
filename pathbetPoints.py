def is_path_dfs(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    
    def dfs(x, y):
        # Check boundaries and if cell is walkable
        if x < 0 or x >= rows or y < 0 or y >= cols or matrix[x][y] == 1 or (x, y) in visited:
            return False
        if (x, y) == end:
            return True
        
        visited.add((x, y))
        
        # Explore all four directions
        return (dfs(x + 1, y) or
                dfs(x - 1, y) or
                dfs(x, y + 1) or
                dfs(x, y - 1))
    
    dfs(start[0], start[1])
    return len(visited)

# Example usage
matrix1 = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]
matrix2 = [
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 0]
]

start = (0, 0)
end = (3, 3)

print(is_path_dfs(matrix1, start, end))  
print(is_path_dfs(matrix2, start, end))  