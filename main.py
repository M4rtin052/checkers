import pygame
from constants import SQUARE_SIZE, WIDTH, HEIGHT
from game import Game

WINDOWS = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Warcaby")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    game = Game(WINDOWS)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    if game.winner() != None:
        print(game.winner())

    pygame.quit()

main()