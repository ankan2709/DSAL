num_rows, num_cols = len(grid), len(grid[0])

def getNeighbors(coord):
    row, col = coord
    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]
    res = []

    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = row + delta_col[i]
        if 0 <= neighbor_row < num_row and 0 <= neighbor_col < num_cols:
            res.append((neighbor_row, neighbor_col))