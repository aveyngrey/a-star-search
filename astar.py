import heapq

finished = False

def distance(point1: tuple[int, int], 
             point2: tuple[int, int]) -> int:
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def astar(grid: tuple[tuple[int, ...], ...], 
          start: tuple[int, int], 
          goal: tuple[int, int]) -> list[tuple[int, int]]:
    rows, cols = len(grid), len(grid[0])
    
    open_set = []
    heapq.heappush(open_set, (0, start)) # f-score, (row, col)

    came_from = {}
    g_score = {start : 0}

    neighbors = [(0,1), (1,0), (0,-1), (-1,0)]

    current_f, current_pos = heapq.heappop(open_set)

    if current_pos == goal:
        path = []
        current_path_pos = goal
        while current_path_pos in came_from:
            path.append(current_path_pos)
            current_path_pos = came_from[current_path_pos]
        path.append(start)
        path.reverse
        return path

    for dr, dc in neighbors:
        neighbor_pos = (current_pos[0] + dr, current_pos[1] + dc)
        neighbor_row, neighbor_col = neighbor_pos

        if (0 <= neighbor_row < rows 
        and 0 <= neighbor_col < cols 
        and grid[neighbor_row][neighbor_col] == 0):
            
            tentative_g = g_score[current_pos] + 1

            if (neighbor_pos not in g_score 
            or tentative_g < g_score[neighbor_pos]):
                came_from[neighbor_pos] = current_pos
                g_score[neighbor_pos] = tentative_g
                f_score = tentative_g + distance(neighbor_pos, goal)
                heapq.heappush(open_set, (f_score, neighbor_pos))
    return []

def print_grid(grid: tuple[tuple[int, ...], ...], 
               path: list[tuple[int, int]], 
               start: tuple[int, int], 
               goal: tuple[int, int]) -> None:
    path_set = set(path) if path else set()
    
    for r in range(len(grid)):
        line = ""
        for c in range(len(grid[r])):
            coord = (r, c)
            if coord == start:
                line += " S "
            elif coord == goal:
                line += " G "
            elif coord in path_set:
                line += " * "
            elif grid[r][c] == 1:
                line += " ■ "
            else:
                line += " . "
        print(line)

if __name__ == "__main__":
    grid = (
        (0, 0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 1, 0, 1, 1, 0),
        (0, 1, 0, 1, 0, 1, 1, 0),
        (0, 1, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 1, 0, 1, 1, 0),
        (0, 1, 0, 0, 0, 1, 1, 0),
        (0, 1, 1, 1, 1, 1, 1, 0),
        (0, 0, 0, 0, 0, 0, 0, 0),
    )
    start = (0,0)
    goal = (7,7)
    path = astar(grid, start, goal)
    print_grid(grid, path, start, goal)
    print(f"Path length: {len(path)}") if path else print("No path found :(")