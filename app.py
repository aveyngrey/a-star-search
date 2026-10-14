import pygame
from cell import Cell
import astar
import maze_generator

pygame.init()
clock = pygame.time.Clock()

def make_grid(rows: int, width: int) -> list[list[Cell]]:
        grid = []
        cell_width = width // rows
        for row in range(rows):
            grid.append([])
            for col in range(rows):
                cell = Cell(row, col, cell_width, rows)
                grid[row].append(cell)
        return grid

def draw_grid(win, rows, width):
    cell_width = width // rows
    for i in range(rows):
        pygame.draw.line(win, pygame.Color("black"), (0, i * cell_width), (width, i * cell_width))
    for j in range(rows):
        pygame.draw.line(win, pygame.Color("black"), (j * cell_width, 0), (j * cell_width, width))

def draw(win, grid, rows, width):
    win.fill("white")

    for row in grid:
        for cell in row:
            cell.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    cell_width = width // rows
    x, y = pos

    row = y // cell_width
    col = x // cell_width

    if row >= rows:
        row = rows - 1
    elif row < 0:
        row = 0

    if col >= rows:
        col = rows - 1
    elif col < 0:
        col = 0

    return row, col

def main(win, rows=21, width=693, fps=60, steps_per_frame=1):
    width = width - (width % rows)
    grid = make_grid(rows, width)

    # keep track of start and goal cells
    start = None
    goal = None

    running = True
    started = False
    done = False

    path_count = 0

    generating_maze = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if not started:
                if pygame.mouse.get_pressed()[0]: # left click
                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(pos, rows, width)
                    cell = grid[row][col]
                    if not start and cell != goal:
                        start = cell
                        cell.set_start()
                    elif not goal and cell != start:
                        goal = cell
                        cell.set_goal()
                    elif cell != start and cell != goal:
                        cell.set_wall()
                elif pygame.mouse.get_pressed()[2]: # right click
                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(pos, rows, width)
                    cell = grid[row][col]
                    if cell == start:
                        start = None
                    elif cell == goal:
                        goal = None
                    cell.reset()
            if event.type == pygame.KEYDOWN and not started:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE] and start and goal:
                    started = True
                    astar.init(grid)
                elif keys[pygame.K_m]:
                    started = True
                    if start is None:
                        start = grid[0][0]
                    if goal is None:
                        goal = grid[rows - 1][rows - 1]
                    maze_generator.init(grid, start.get_pos(), goal.get_pos())
                    generating_maze = True

        if generating_maze:
            for _ in range(steps_per_frame):
                maze_generator.step()
            generating_maze = maze_generator.is_active()
            if not generating_maze:
                astar.init(grid)
        elif started and not done:
            for _ in range(steps_per_frame):
                astar.astar()
                if astar.is_finished():
                    break
            if astar.is_finished():
                done = True
            elif astar.no_path():
                done = True

        path = astar.get_path()
        if done and (path_count < len(path)):
            path_pos = path[path_count]
            path_row, path_col = path_pos
            path_cell = grid[path_row][path_col]
            if path_cell != start and path_cell != goal:
                path_cell.set_path()
            if path_count == len(path) - 1:
                print(f"Path Length: {len(path) - 1}")
            path_count += 1

        win.fill("gray", pygame.Rect(0, 0, width, width))
    
        draw(win, grid, rows, width)
    
        pygame.display.flip()
    
        clock.tick(fps)

    pygame.quit()
