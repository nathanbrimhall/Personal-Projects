import sys
import pygame as pg

pg.init()
screen_size = 470, 470
screen = pg.display.set_mode(screen_size)
font = pg.font.SysFont(None, 15)

def draw_background():
    screen.fill(pg.Color("White"))
    pg.draw.rect(screen, pg.Color("black"), pg.Rect(10, 10, 450, 450), 4)
    for i in range(1, 9):
        linewidth = 4 if i % 3 == 0 else 2
        x = 10 + i * 50
        # Vertical lines
        pg.draw.line(screen, pg.Color("black"), (x, 10), (x, 460), linewidth)
        # Horizontal lines
        pg.draw.line(screen, pg.Color("black"), (10, x), (460, x), linewidth)

def draw_numbers():
    pass
    """I think that this function should draw upon the grid..."""



def game_loop():
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    draw_background()
    pg.display.flip()

run = True
while run:
    game_loop()