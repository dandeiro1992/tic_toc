from Player import *

black = (0, 0, 0)
red = (255, 0, 0)
bar_width = 5
info_height = 150


class Game:
    turn = False

    def initGraphics(self):
        self.Blank = pygame.image.load("obrazki/Blank.jpg")
        self.Circle = pygame.image.load("obrazki/Circle.png")
        self.Cross = pygame.image.load("obrazki/Cross.png")
        self.circle = pygame.image.load("obrazki/circle.png")
        self.cross = pygame.image.load("obrazki/cross.png")
        self.Blank_width = self.Blank.get_rect().size[0]
        self.Blank_height = self.Blank.get_rect().size[1]
        self.board = [[0 for x in range(3)] for y in range(3)]

    def drawBoard(self):
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == 0:
                    self.screen.blit(self.Blank, [x * self.Blank_width + (x + 1) * bar_width,
                                                  y * self.Blank_height + (y + 1) * bar_width])
                elif self.board[x][y] == 1:
                    self.screen.blit(self.Circle, [x * self.Blank_width + (x + 1) * bar_width,
                                                   y * self.Blank_height + (y + 1) * bar_width])
                else:
                    self.screen.blit(self.Cross, [x * self.Blank_width + (x + 1) * bar_width,
                                                  y * self.Blank_height + (y + 1) * bar_width])
        restart = pygame.draw.rect(self.screen, red,
                                   (self.screen.get_rect().size[0] / 2 - 50, self.screen.get_rect().size[1] - 110, 100,
                                    50))
        myfont = pygame.font.SysFont(None, 31)
        self.screen.blit(myfont.render("RESTART", 1, black),
                         (self.screen.get_rect().size[0] / 2 - 50, self.screen.get_rect().size[1] - 100))

    def __init__(self):
        self.initGraphics()
        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.Blank_width * 3 + 4 * bar_width, self.Blank_height * 3 + 4 * bar_width + info_height))
        pygame.display.set_caption("Kółko i Krzyżyk")
        pygame.font.init()
        self.player_A = Player("circle", self.screen)
        self.player_B = Player("cross", self.screen)

    def draw_info(self):
        myfont = pygame.font.SysFont(None, 32)
        label = myfont.render("Your Turn:", 1, (255, 255, 255))
        self.screen.blit(label, (10, self.Blank_height * 3 + 8 * bar_width))
        if self.turn:
            self.screen.blit(self.cross, (label.get_rect().size[0] + 15, self.Blank_height * 3 + 6 * bar_width))
        else:
            self.screen.blit(self.circle, (label.get_rect().size[0] + 15, self.Blank_height * 3 + 6 * bar_width))

    def update(self):
        self.screen.fill(black)
        if self.turn:
            self.board, pressed = self.player_B.press_mouse(self.board)
            if pressed:
                self.turn = False
        else:
            self.board, pressed = self.player_A.press_mouse(self.board)
            if pressed:
                self.turn = True
        self.drawBoard()
        self.draw_info()
        pygame.display.update()
        for event in pygame.event.get():
            # quit if the quit button was pressed
            if event.type == pygame.QUIT:
                exit()
        mouse = pygame.mouse.get_pos()
