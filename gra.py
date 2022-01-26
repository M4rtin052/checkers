import pygame
from stałe import COBALTGREEN, DARKOLIVEGREEN, SQUARE_SIZE, RED
from plansza import Board

class Game:
    def __init__(self, win):
        self.mech()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def mech(self):
        self.selected = None
        self.board = Board()
        self.turn = COBALTGREEN
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self.mech()

    def select(self, row, col):
        if self.selected:
            result = self.move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def move (self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
       for move in moves:
            row, col = move
            pygame.draw.circle(self.win, RED, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 7)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == DARKOLIVEGREEN:
            self.turn = COBALTGREEN
        else:
            self.turn = DARKOLIVEGREEN