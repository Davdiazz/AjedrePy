import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (173, 216, 230)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    font = pygame.font.SysFont(None, 72)
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != " ":
                color = BLUE if piece.isupper() else BLACK
                piece_text = font.render(piece, True, color)
                screen.blit(piece_text, (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + 10))

def is_valid_move(piece, start_pos, end_pos):
    return True

def main():
    selected_piece = None
    turn = "white"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                row, col = event.pos[1] // SQUARE_SIZE, event.pos[0] // SQUARE_SIZE
                if selected_piece:
                    if is_valid_move(selected_piece, selected_piece[1], (row, col)):
                        board[row][col] = board[selected_piece[1][0]][selected_piece[1][1]]
                        board[selected_piece[1][0]][selected_piece[1][1]] = " "
                        turn = "black" if turn == "white" else "white"
                    selected_piece = None
                else:
                    piece = board[row][col]
                    if (turn == "white" and piece.isupper()) or (turn == "black" and piece.islower()):
                        selected_piece = (piece, (row, col))

        draw_board()
        draw_pieces()
        pygame.display.flip()

# Llamamos a la función principal para iniciar el juego
main()
