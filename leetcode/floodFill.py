n_rows, n_cols = len(image), len(image[0])


def get_neighbors(coord, color):
    row, col = coord
    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]

    for i in range(len(delta_row)):
        neigh_row = row + delta_row[i]
        neigh_col = col + delta_col[i]

        if 0 <= neigh_row < n_rows and 0 <= neigh_col < n_cols:
            if image[neigh_row][neigh_col] == color:
                yield neigh_row, neigh_col


def bfs(root):
    queue = collection.deque()
    visited = [[False for c in range(n_cols)] for r in range(n_rows)]
    queue.append(root)
    r, c = root
    image[r][c] = replacement
    visited[r][c] = True

    while queue:
        node = queue.popleft()
        for neighbor in get_neighbors(node):
            r, c = neighbor
            if visited[r][c]:
                continue
            image[r][c] = replacement
            queue.append(neighbor)
            visited[r][c] = True

    