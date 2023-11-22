import pygame
import sys
from window import GameWindow

class ChessGame:
    def __init__(self):
        pygame.init()
        self.game_window = GameWindow()
        self.running = True
        self.board = self.initialize_board()
        self.current_turn = 'white'

    def run(self):
        print(self.board)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.game_logic()
            self.game_window.update()

        pygame.quit()
        sys.exit()
        
    def initialize_board(self):
        return [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
                ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
        
    def game_logic(self):
        pass