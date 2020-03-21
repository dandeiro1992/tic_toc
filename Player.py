import pygame
import math


class Player:
    name = "gracz"
    value = 0
    def __init__(self, name, screen, nickname="Ola"):
        self.screen = screen
        self.name = name
        self.nickname = nickname
        if name == "circle":
            self.value = 2
        else:
            self.value = 25

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
            board[xpos][ypos] = 2
            pressed = True
        elif pygame.mouse.get_pressed()[0] and out_of_bounds == False and board[xpos][
            ypos] == 0 and self.name == "cross":
            board[xpos][ypos] = 25
            pressed = True
        return board, pressed
