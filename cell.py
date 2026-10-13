import pygame

# color constants
EMPTY_COLOR = pygame.Color("lightgray")
OPEN_COLOR = pygame.Color("purple")
CLOSED_COLOR = pygame.Color("lightpink")
START_COLOR = pygame.Color("green")
GOAL_COLOR = pygame.Color("yellow") 
WALL_COLOR = pygame.Color("black")
PATH_COLOR = pygame.Color("blue")
MAZE_GENERATE_COLOR = pygame.Color("cyan")

def init_colors(empty_color, open_color, closed_color, start_color,
                goal_color, wall_color, path_color) -> None:
    global EMPTY_COLOR, OPEN_COLOR, CLOSED_COLOR, START_COLOR, \
           GOAL_COLOR, WALL_COLOR, PATH_COLOR
    EMPTY_COLOR = empty_color
    OPEN_COLOR = open_color
    CLOSED_COLOR = closed_color
    START_COLOR = start_color
    GOAL_COLOR = goal_color
    WALL_COLOR = wall_color
    PATH_COLOR = path_color

class Cell:

    def __init__(self, row: int, col: int, width: int, total_rows: int) -> None:
        self.row = row
        self.col = col
        self.x = col * width
        self.y = row * width
        self.color = EMPTY_COLOR
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def set_maze_generate_highlight(self) -> None:
        self.color = MAZE_GENERATE_COLOR

    def get_pos(self) -> tuple[int, int]:
        return self.row, self.col

    def is_closed(self) -> bool:
        return self.color == CLOSED_COLOR

    def is_open(self) -> bool:
        return self.color == OPEN_COLOR

    def is_start(self) -> bool:
        return self.color == START_COLOR

    def is_goal(self) -> bool:
        return self.color == GOAL_COLOR

    def is_wall(self) -> bool:
        return self.color == WALL_COLOR

    def is_empty(self) -> bool:
        return self.color == EMPTY_COLOR

    def reset(self) -> None:
        self.color = EMPTY_COLOR

    def set_wall(self) -> None:
        self.color = WALL_COLOR

    def set_open(self) -> None:
        self.color = OPEN_COLOR

    def set_closed(self) -> None:
        self.color = CLOSED_COLOR

    def set_start(self) -> None:
        self.color = START_COLOR

    def set_goal(self) -> None:
        self.color = GOAL_COLOR

    def set_path(self) -> None:
        self.color = PATH_COLOR

    def draw(self, win) -> None:
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
