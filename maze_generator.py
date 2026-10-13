from cell import Cell
import random
import pygame

grid = []
generator_active = False
generator_path = []
neighbors = []
current_cell: Cell | None = None
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
start = (0, 0)
goal = (0, 0)

def init(grid: list[list[Cell]], start: tuple[int, int], goal: tuple[int, int]) -> None:
    globals()["grid"] = grid
    globals()["start"] = start
    globals()["goal"] = goal
    global neighbors, generator_active, generator_path, current_cell

    rows = len(grid)
    for row in grid:
        for cell in row:
            if cell.get_pos() == start:
                cell.set_start()
            elif cell.get_pos() == goal:
                cell.set_goal()
            else:
                cell.set_wall()

    current_pos = (random.randrange(0, rows), random.randrange(0, rows))
    while current_pos == start or current_pos == goal:
        current_pos = (random.randrange(0, rows), random.randrange(0, rows))
    current_row, current_col = current_pos
    current_cell = grid[current_row][current_col]
    current_cell.reset()
    current_cell.set_maze_generate_highlight()


    neighbors = wall_neighbors(current_pos)
    generator_path.append(grid[current_row][current_col])
    generator_active = True
    

def step() -> None:
    global neighbors, generator_path, generator_active, current_cell

    if not generator_active:
        return

    if current_cell is None:
        raise RuntimeError("Generator has no current cell")

    current_cell.reset()
    if neighbors:
        rand_index = random.randrange(0, len(neighbors))
        next_cell = neighbors[rand_index]
        next_cell.reset()
        next_cell.set_maze_generate_highlight()
        generator_path.append(next_cell)
        neighbors = wall_neighbors(next_cell.get_pos())
        current_cell = next_cell
    elif generator_path:
        last_cell = generator_path.pop()
        neighbors = wall_neighbors(last_cell.get_pos())
        last_cell.set_maze_generate_highlight()
        current_cell = last_cell
    else:
        for dr, dc in directions:
            row, col = start[0] + dr, start[1] + dc
            if not (0 <= row < len(grid) and 0 <= col < len(grid)):
                continue
            grid[row][col].reset()

        for dr, dc in directions:
            row, col = goal[0] + dr, goal[1] + dc
            if not (0 <= row < len(grid) and 0 <= col < len(grid)):
                continue
            grid[row][col].reset()

        generator_active = False

def is_active() -> bool:
    return generator_active

def wall_neighbors(pos: tuple[int, int]) -> list[Cell]:
    current_row, current_col = pos
    neighbor_list = []
    for dr, dc in directions:
        neighbor_row, neighbor_col = current_row + dr, current_col + dc
        if not (0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid)):
            continue
        neighbor_cell = grid[neighbor_row][neighbor_col]
        if neighbor_cell.is_wall():
            for dr, dc in directions:
                row, col = neighbor_row + dr, neighbor_col + dc
                if not (0 <= row < len(grid) and 0 <= col < len(grid)):
                    continue
                if (row, col) != pos and grid[row][col].is_empty():
                    break
            else:
                neighbor_list.append(neighbor_cell)
    return neighbor_list
        
