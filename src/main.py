from collections import deque


def find_shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    queue = deque([(start, 0)])
    path = [[-1] * cols for _ in range(rows)]
    path[start[0]][start[1]] = -2

    while queue:
        (x, y), dist = queue.popleft()

        if (x, y) == end:
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == 1 and path[nx][ny] == -1:
                path[nx][ny] = i
                queue.append(((nx, ny), dist + 1))

    x, y = end
    shortest_path = []
    while (x, y) != start:
        i = path[x][y]
        shortest_path.append(i)
        x -= dx[i]
        y -= dy[i]

    shortest_path.reverse()
    return len(shortest_path)


with open("src/input.txt", "r") as file:
    start = tuple(map(int, file.readline().strip().split(", ")))
    end = tuple(map(int, file.readline().strip().split(", ")))
    rows, cols = map(int, file.readline().strip().split(", "))
    matrix = []
    for _ in range(rows):
        line = list(map(int, file.readline().strip().split()))
        matrix.append(line)

path_length = find_shortest_path(matrix, start, end)

with open("src/output.txt", "w") as file:
    file.write(str(path_length))
