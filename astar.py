import heapq
from cell import Cell

# general globals

finished = False
path = []
grid = None
cell_grid = None
start = (0, 0)
goal = None

# globals to save values after each astar() call
open_set = []
came_from = {}
g_score = {}
count = 0

def init(init_grid) -> None:
    global grid, start, goal, cell_grid
    cell_grid = init_grid
    temp_grid = []
    for row in range(len(init_grid)):
        temp_grid.append([])
        for col in range(len(init_grid[0])):
            cell = init_grid[row][col]
            if not cell.is_wall():
                temp_grid[row].append(0)
                if cell.is_start():
                    start = cell.get_pos()
                elif cell.is_goal():
                    goal = cell.get_pos()
            elif not cell.is_start() and not cell.is_goal():
                temp_grid[row].append(1)
    grid = tuple(tuple(row) for row in temp_grid)

def distance(point1: tuple[int, int], 
             point2: tuple[int, int]) -> int:
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def astar() -> None:
    global grid, start, goal, finished, cell_grid
    global open_set, g_score, came_from, count

    if grid is None:
        raise RuntimeError("grid has not been initialized")
    if not grid:
        raise ValueError("grid must not be empty")

    if goal is None:
        raise RuntimeError("goal has not been initialized")
    if not goal:
        raise ValueError("goal must not be empty")

    if cell_grid is None:
        raise RuntimeError("cell_grid has not been initialized")
    if not cell_grid:
        raise ValueError("cell_grid must not be empty")

    if g_score is None:
        raise RuntimeError("g_score has not been initialized")

    if count == 0:
        g_score[start] = 0

        # f-score, h-score, (row, col)
        heapq.heappush(open_set, (0, distance(start, goal), start))

    # exit function if no path exists
    if count > 0 and not open_set:
        return
    
    rows, cols = len(grid), len(grid[0])
    
    neighbors = [(0,1), (1,0), (0,-1), (-1,0)]

    current_pos = heapq.heappop(open_set)[2]
    current_row, current_col = current_pos
    current_cell = cell_grid[current_row][current_col]
    if current_pos != start and current_pos != goal:
        current_cell.set_closed()

    if current_pos == goal:
        global path
        path = []
        current_path_pos = goal
        while current_path_pos in came_from:
            path.append(current_path_pos)
            current_path_pos = came_from[current_path_pos]
        path.reverse()
        finished = True
        return

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
                h_score = distance(neighbor_pos, goal)
                f_score = tentative_g + h_score
                heapq.heappush(open_set, (f_score, h_score, neighbor_pos))
                neighbor_cell = cell_grid[neighbor_row][neighbor_col]
                if neighbor_pos != start and neighbor_pos != goal:
                    neighbor_cell.set_open()

    count += 1

def is_finished() -> bool:
    return finished

def no_path() -> bool:
    return not open_set

def get_path() -> list[tuple[int, int]]:
    return path