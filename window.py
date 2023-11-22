import pygame
       
class GameWindow:
    def __init__(self):
        self.size = (800, 600)
        self.window = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Chess Game")
    
    def draw_board(self, board):
        for row in range(8):
            for col in range(8):
                square_color = (255, 255, 255) if (row + col) % 2 == 0 else (0, 0, 0)
                pygame.draw.rect(self.window, square_color, (col * self.square_size, row * self.square_size, self.square_size, self.square_size))
                
                piece = board[row][col]
                if piece != '.':
                    # self.window.blit(piece_image, (col * self.square_size, row * self.square_size))
                    # intitializing the piece
                    pass

    def update(self, board):
        self.draw_board(board)
        pygame.display.update()

