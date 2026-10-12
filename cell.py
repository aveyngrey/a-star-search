import pygame

# color constants
EMPTY = pygame.Color("lightgray")
OPEN = pygame.Color("purple")
CLOSED = pygame.Color("lightpink")
START = pygame.Color("green")
GOAL = pygame.Color("yellow") 
WALL = pygame.Color("black")
PATH = pygame.Color("blue")


class Cell:

    def __init__(self, row, col, width, total_rows) -> None:
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = EMPTY

    def make_wall(self):
        pass

    def set_open(self):
        pass

    def set_closed(self):
        pass

    def set_start(self):
        pass

    def set_goal(self):
        pass

    def reset(self):
        pass