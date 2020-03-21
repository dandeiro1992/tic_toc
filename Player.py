import pygame
import math


class Player:
    name = "gracz"

    def __init__(self, name, screen):
        self.screen = screen
        self.name = name

    def press_mouse(self, board):
        pressed = False
        out_of_bounds = False
        mouse = pygame.mouse.get_pos()
        xpos = int(math.floor((mouse[0] / 205)))
        ypos = int(math.floor((mouse[1] / 205)))
        if (mouse[0] > 620) or mouse[1] > 620:
            out_of_bounds = True
        if pygame.mouse.get_pressed()[0] and out_of_bounds == False and board[xpos][
            ypos] == 0 and self.name == "circle":
            board[xpos][ypos] = 1
            pressed = True
        elif pygame.mouse.get_pressed()[0] and out_of_bounds == False and board[xpos][
            ypos] == 0 and self.name == "cross":
            board[xpos][ypos] = 2
            pressed = True
        return board, pressed
