import sys
import pygame
from main import board

# Define some colors
Brown = (139, 69, 19)
WHITE = (255, 233, 197)

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 750
screen_height = 750
screen = pygame.display.set_mode([screen_width, screen_height])

# Set the dimensions of the board
board_size = 750
board_width = board_size
board_height = board_size

# Create a surface for the board
board_surface = pygame.Surface([board_width, board_height])

# Draw the board
for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            color = WHITE
        else:
            color = Brown
        pygame.draw.rect(board_surface, color, [col * (board_size/8), row * (board_size/8), (board_size/8), (board_size/8)])

# Set the position of the board on the screen
board_x = (screen_width - board_width) // 2
board_y = (screen_height - board_height) // 2

# Load the images for the checkers and scale them down
DD = pygame.image.load('pics/darkpng.png')
DW = pygame.image.load('pics/whitepng.png')
DW = pygame.transform.scale(DW, (int(board_size/8), int(board_size/8)))
DD = pygame.transform.scale(DD, (int(board_size/8), int(board_size/8)))

# Place the checkers on the board
for row in range(8):
    for col in range(8):
        if board[row][col] == 'DW':
            board_surface.blit(DW, (col * (board_size/8), row * (board_size/8)))
        elif board[row][col] == 'DD':
            board_surface.blit(DD, (col * (board_size/8), row * (board_size/8)))

# Draw the board on the screen
screen.blit(board_surface, [board_x, board_y])

# Update the display
pygame.display.flip()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()