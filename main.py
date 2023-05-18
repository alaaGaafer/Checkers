import time
import random
import pygame
import sys


def level_selection():
    # Initialize Pygame
    pygame.init()

    # Set up the screen
    screen_width = 750
    screen_height = 750
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Game Configuration")

    # Define colors
    BROWN = (139, 69, 19)
    WHITE = (255, 233, 197)
    BLACK = (0, 0, 0)

    # Define font
    font = pygame.font.Font(None, 32)

    # Initialize level, strategy, and algorithm selection
    level = None
    strategy = None
    algorithm = None

    # Load header image
    header_image = pygame.image.load("pics/bar2.png")

    # Create level section
    level_section = pygame.Rect(150, 350, screen_width - 280, 125)
    level_title = font.render("Levels", True, BLACK)
    level_title_rect = level_title.get_rect(center=(level_section.centerx, level_section.top + 30))

    easy_button = pygame.Rect(level_section.left + 20, level_section.top + 70, 20, 20)
    medium_button = pygame.Rect(level_section.left + 180, level_section.top + 70, 20, 20)
    hard_button = pygame.Rect(level_section.left + 340, level_section.top + 70, 20, 20)

    # Create strategy section
    strategy_section = pygame.Rect(50, 100, screen_width // 2 - 70, 200)
    strategy_title = font.render("Strategies", True, BLACK)
    strategy_title_rect = strategy_title.get_rect(center=(strategy_section.centerx, strategy_section.top + 30))

    plot_attack_button = pygame.Rect(strategy_section.left + 20, strategy_section.top + 70, 20, 20)
    attack_button = pygame.Rect(strategy_section.left + 20, strategy_section.top + 120, 20, 20)

    # Create algorithm section
    algorithm_section = pygame.Rect(screen_width // 2 + 30, 100, screen_width // 2 - 70, 200)
    algorithm_title = font.render("Algorithms", True, BLACK)
    algorithm_title_rect = algorithm_title.get_rect(center=(algorithm_section.centerx, algorithm_section.top + 30))

    minimax_button = pygame.Rect(algorithm_section.left + 20, algorithm_section.top + 70, 20, 20)
    alpha_beta_button = pygame.Rect(algorithm_section.left + 20, algorithm_section.top + 120, 20, 20)

    # Create Play button
    play_button = pygame.Rect(level_section.centerx - 50, level_section.bottom + 30, 100, 50)
    play_text = font.render("Play", True, WHITE)
    play_text_rect = play_text.get_rect(center=play_button.center)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Check if the level buttons are clicked
                if easy_button.collidepoint(mouse_pos):
                    level = 1
                elif medium_button.collidepoint(mouse_pos):
                    level = 2
                elif hard_button.collidepoint(mouse_pos):
                    level = 3

                # Check if the strategy buttons are clicked
                if plot_attack_button.collidepoint(mouse_pos):
                    strategy = "Plot"
                elif attack_button.collidepoint(mouse_pos):
                    strategy = "Attack"

                # Check if the algorithm buttons are clicked
                if minimax_button.collidepoint(mouse_pos):
                    algorithm = "Minimax"
                elif alpha_beta_button.collidepoint(mouse_pos):
                    algorithm = "Alpha"

                # Check if the Play button is clicked
                if play_button.collidepoint(mouse_pos):
                    if level is not None and strategy is not None and algorithm is not None and level != 0:
                        running = False

        # Fill the screen with background color
        screen.fill(WHITE)

        # Draw header image
        screen.blit(header_image, (5, -10))

        # Draw the level section
        pygame.draw.rect(screen, BLACK, level_section, 2)
        screen.blit(level_title, level_title_rect)
        pygame.draw.rect(screen, BROWN if level == 1 else BLACK, easy_button, width=2 if level != 1 else 0)
        pygame.draw.rect(screen, BROWN if level == 2 else BLACK, medium_button, width=2 if level != 2 else 0)
        pygame.draw.rect(screen, BROWN if level == 3 else BLACK, hard_button, width=2 if level != 3 else 0)
        easy_text = font.render("Easy", True, BLACK)
        easy_text_rect = easy_text.get_rect()
        easy_text_rect.center = easy_button.center
        screen.blit(easy_text, (easy_button.right + 10, easy_button.centery - easy_text.get_height() // 2))
        medium_text = font.render("Medium", True, BLACK)
        medium_text_rect = medium_text.get_rect()
        medium_text_rect.center = medium_button.center
        screen.blit(medium_text, (medium_button.right + 10, medium_button.centery - medium_text.get_height() // 2))
        hard_text = font.render("Hard", True, BLACK)
        hard_text_rect = hard_text.get_rect()
        hard_text_rect.center = hard_button.center
        screen.blit(hard_text, (hard_button.right + 10, hard_button.centery - hard_text.get_height() // 2))

        # Draw the strategy section
        pygame.draw.rect(screen, BLACK, strategy_section, 2)
        screen.blit(strategy_title, strategy_title_rect)
        pygame.draw.rect(screen, BROWN if strategy == "Plot" else BLACK, plot_attack_button, width=2 if strategy != "Plot" else 0)
        pygame.draw.rect(screen, BROWN if strategy == "Attack" else BLACK, attack_button, width=2 if strategy != "Attack" else 0)
        plot_attack_text = font.render("Plot and Attack", True, BLACK)
        plot_attack_text_rect = plot_attack_text.get_rect()
        plot_attack_text_rect.midleft = (plot_attack_button.right + 10, plot_attack_button.centery)
        screen.blit(plot_attack_text, plot_attack_text_rect)
        attack_text = font.render("Attack", True, BLACK)
        attack_text_rect = attack_text.get_rect()
        attack_text_rect.midleft = (attack_button.right + 10, attack_button.centery)
        screen.blit(attack_text, attack_text_rect)

        # Draw the algorithm section
        pygame.draw.rect(screen, BLACK, algorithm_section, 2)
        screen.blit(algorithm_title, algorithm_title_rect)
        pygame.draw.rect(screen, BROWN if algorithm == "Minimax" else BLACK, minimax_button, width=2 if algorithm != "Minimax" else 0)
        pygame.draw.rect(screen, BROWN if algorithm == "Alpha" else BLACK, alpha_beta_button, width=2 if algorithm != "Alpha" else 0)
        minimax_text = font.render("Minimax", True, BLACK)
        minimax_text_rect = minimax_text.get_rect()
        minimax_text_rect.midleft = (minimax_button.right + 10, minimax_button.centery)
        screen.blit(minimax_text, minimax_text_rect)
        alpha_beta_text = font.render("Alpha-Beta", True, BLACK)
        alpha_beta_text_rect = alpha_beta_text.get_rect()
        alpha_beta_text_rect.midleft = (alpha_beta_button.right + 10, alpha_beta_button.centery)
        screen.blit(alpha_beta_text, alpha_beta_text_rect)

        # Draw the Play button
        pygame.draw.rect(screen, BROWN, play_button)
        screen.blit(play_text, play_text_rect)

        # Update the display
        pygame.display.flip()

    # Return the selected level, strategy, and algorithm
    return level, strategy, algorithm




def start_gui(Board):
    Brown = (139, 69, 19)
    WHITE = (255, 233, 197)
    DarkPieces = sum(row.count("DD") + row.count("DDK") for row in Board)
    WhitePieces = sum(row.count("DW") + row.count("DWK") for row in Board)

    # Initialize Pygame
    pygame.init()

    # Set the dimensions of the screen
    screen_width = 725
    screen_height = 800  # Increased height to fill the bottom plank space
    screen = pygame.display.set_mode([screen_width, screen_height])

    # Set the dimensions of the board
    board_size = 725
    board_width = board_size
    board_height = board_size

    # Create a surface for the board
    board_surface = pygame.Surface([board_width, board_height])
    header_image = pygame.image.load("pics/count.png")
    # Get the dimensions of the image
    image_width = header_image.get_width()
    image_height = header_image.get_height()

    # Set the position to write the numbers (middle of the image)
    number_x = image_width // 2
    number_y = image_height // 2

    # Set the font and size for the numbers
    font = pygame.font.Font(None, 36)

    # Render the numbers as text
    whitecount = font.render(str(WhitePieces), True, (0, 0, 0))  # Replace "123" with the desired number
    darkcount = font.render(str(DarkPieces), True, (0, 0, 0))  # Replace "123" with the desired number

    # Get the dimensions of the rendered text
    text_width = whitecount.get_width()
    text_height = whitecount.get_height()

    # Calculate the position to blit the numbers (centered)
    number_pos_x = number_x - (text_width // 2)
    number_pos_y = number_y - (text_height // 2)

    # Blit the image onto the screen
    # Blit the numbers onto the screen
    screen.blit(header_image, (-5, -20))
    screen.blit(darkcount, (number_pos_x-115, number_pos_y-30))
    screen.blit(whitecount, (number_pos_x-45, number_pos_y-30))


    # Draw the board
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = Brown
            pygame.draw.rect(board_surface, color,[col * (board_size / 8), row * (board_size / 8), (board_size / 8), (board_size / 8)])

    # Set the position of the board on the screen
    board_x = (screen_width - board_width) // 2
    board_y = 55

    # Load the images for the checkers and scale them down
    DD = pygame.image.load('pics/darkpng.png')
    DW = pygame.image.load('pics/whitepng.png')
    DDK = pygame.image.load('pics/darkKing.png')
    DWK = pygame.image.load('pics/WhiteKing.png')
    DW = pygame.transform.scale(DW, (int(board_size / 8), int(board_size / 8)))
    DD = pygame.transform.scale(DD, (int(board_size / 8), int(board_size / 8)))
    DDK = pygame.transform.scale(DDK, (int(board_size / 8), int(board_size / 8)))
    DWK = pygame.transform.scale(DWK, (int(board_size / 8), int(board_size / 8)))

    # Place the checkers on the board
    for row in range(8):
        for col in range(8):
            if board[row][col] == 'DW':
                board_surface.blit(DW, (col * (board_size / 8), row * (board_size / 8)))
            elif board[row][col] == 'DD':
                board_surface.blit(DD, (col * (board_size / 8), row * (board_size / 8)))
            elif board[row][col] == 'DDK':
                board_surface.blit(DDK, (col * (board_size / 8), row * (board_size / 8)))
            elif board[row][col] == 'DWK':
                board_surface.blit(DWK, (col * (board_size / 8), row * (board_size / 8)))

    # Draw the board on the screen
    screen.blit(board_surface, [board_x, board_y])

    # Update the display
    pygame.display.flip()



def create_board():
    # Board = [
    #       0     1     2     3    4     5    6     7
    #     0["W", "DD", "W", "DD", "W", "DD", "W", "DD"],
    #     1["DD", "W", "D", "W", "DD", "W", "DD", "W"],
    #     2["W", "DD", "W", "D", "W", "DD", "W", "DD"],
    #     3["D", "W", "D", "W", "D", "W", "D", "W"],
    #     4["W", "DD", "W", "D", "W", "D", "W", "D"],
    #     5["D", "W", "D", "W", "DW", "W", "DW", "W"],
    #     6["W", "DD", "W", "DW", "W", "DW", "W", "DW"],
    #     7["DW", "W", "DW", "W", "DW", "W", "DW", "W"]
    # ]
    Board = [["W", "DD", "W", "DD", "W", "DD", "W", "DD"],
             ["DD", "W", "DD", "W", "DD", "W", "DD", "W"],
             ["W", "DD", "W", "DD", "W", "DD", "W", "DD"],
             ["D", "W", "D", "W", "D", "W", "D", "W"],
             ["W", "D", "W", "D", "W", "D", "W", "D"],
             ["DW", "W", "DW", "W", "DW", "W", "DW", "W"],
             ["W", "DW", "W", "DW", "W", "DW", "W", "DW"],
             ["DW", "W", "DW", "W", "DW", "W", "DW", "W"]
             ]

    return Board


def small_legal_moves(board, player):
    legal_moves = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == player or board[row][col] == player + "K":
                # check for valid diagonal moves
                if player == "DD":
                    # Dark king reverse moves
                    if board[row][col] == player + 'K':
                        if row > 0 and col > 0 and board[row - 1][col - 1] == "D":
                            legal_moves.append([(row, col), (row - 1, col - 1)])
                        if row > 0 and col < 7 and board[row - 1][col + 1] == "D":
                            legal_moves.append([(row, col), (row - 1, col + 1)])
                        if row > 1 and col > 1 and (
                                board[row - 1][col - 1].startswith("DW") or board[row - 1][col - 1].startswith(
                                "DWK")) and board[row - 2][
                            col - 2] == "D":
                            legal_moves.append([(row, col), (row - 2, col - 2)])
                        if row > 1 and col < 6 and (
                                board[row - 1][col + 1].startswith("DW") or board[row - 1][col + 1].startswith(
                                "DWK")) and board[row - 2][
                            col + 2] == "D":
                            legal_moves.append([(row, col), (row - 2, col + 2)])
                    # Dark king reverse moves
                    # dark pieces moves
                    if row < 7 and col > 0 and board[row + 1][col - 1] == "D":
                        legal_moves.append([(row, col), (row + 1, col - 1)])
                    if row < 7 and col < 7 and board[row + 1][col + 1] == "D":
                        legal_moves.append([(row, col), (row + 1, col + 1)])
                    if row < 6 and col > 1 and (
                            board[row + 1][col - 1].startswith("DW") or board[row + 1][col - 1].startswith("DWK")) and \
                            board[row + 2][col - 2] == "D":
                        legal_moves.append(((row, col), (row + 2, col - 2)))
                    if row < 6 and col < 6 and (
                            board[row + 1][col + 1].startswith("DW") or board[row + 1][col + 1].startswith("DWK")) and \
                            board[row + 2][col + 2] == "D":
                        legal_moves.append([(row, col), (row + 2, col + 2)])
                    # dark pieces moves
                elif player == "DW":
                    # White king reverse moves
                    if board[row][col] == player + 'K':
                        if row < 7 and col > 0 and board[row + 1][col - 1] == "D":
                            legal_moves.append([(row, col), (row + 1, col - 1)])
                        if row < 7 and col < 7 and board[row + 1][col + 1] == "D":
                            legal_moves.append([(row, col), (row + 1, col + 1)])
                        if row < 6 and col > 1 and (
                                board[row + 1][col - 1].startswith("DD") or board[row + 1][col - 1].startswith(
                                "DDK")) and board[row + 2][col - 2] == "D":
                            legal_moves.append(((row, col), (row + 2, col - 2)))
                        if row < 6 and col < 6 and (
                                board[row + 1][col + 1].startswith("DD") or board[row + 1][col + 1].startswith(
                                "DDK")) and board[row + 2][col + 2] == "D":
                            legal_moves.append([(row, col), (row + 2, col + 2)])
                    # White king reverse moves
                    # White pieces moves
                    if row > 0 and col > 0 and board[row - 1][col - 1] == "D":
                        legal_moves.append([(row, col), (row - 1, col - 1)])
                    if row > 0 and col < 7 and board[row - 1][col + 1] == "D":
                        legal_moves.append([(row, col), (row - 1, col + 1)])
                    if row > 1 and col > 1 and (
                            board[row - 1][col - 1].startswith("DD") or board[row - 1][col - 1].startswith("DDK")) and \
                            board[row - 2][col - 2] == "D":
                        legal_moves.append([(row, col), (row - 2, col - 2)])
                    if row > 1 and col < 6 and (
                            board[row - 1][col + 1].startswith("DD") or board[row - 1][col + 1].startswith("DDK")) and \
                            board[row - 2][col + 2] == "D":
                        legal_moves.append([(row, col), (row - 2, col + 2)])
                    # White pieces moves
    return legal_moves


def get_legal_moves(board, player):
    legal_moves = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == player or board[row][col] == player + "K":
                # check for valid diagonal moves
                if player == "DD":
                    if board[row][col] == player + 'K':
                        if board[row][col] == player + 'K':
                            # Dark King moves
                            # -----------------------------------------------------------------------------------------
                            if row > 0 and col > 0 and board[row - 1][col - 1] == "D":
                                legal_moves.append([(row, col), (row - 1, col - 1)])
                            if row > 0 and col < 7 and board[row - 1][col + 1] == "D":
                                legal_moves.append([(row, col), (row - 1, col + 1)])
                            # first left eat(First cond)
                            if row > 1 and col > 1 and (
                                    board[row - 1][col - 1].startswith("DW") or board[row - 1][col - 1].startswith(
                                "DWK")) and board[row - 2][
                                col - 2] == "D":
                                legal_moves.append([(row, col), (row - 2, col - 2)])
                                newRow = row - 2
                                newCol = col - 2
                                # second right eat
                                if newRow > 1 and newCol < 6 and (
                                        board[newRow - 1][newCol + 1].startswith("DW") or board[newRow - 1][
                                    newCol + 1].startswith("DWK")) and \
                                        board[newRow - 2][newCol + 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                                    newRow = newRow - 2
                                    newCol = newCol + 2
                                    # third right eat
                                    if row > 1 and col < 6 and (
                                            board[newRow - 1][newCol + 1].startswith("DW") or board[newRow - 1][
                                        newCol + 1].startswith("DWK")) and \
                                            board[newRow - 2][newCol + 2] == "D":
                                        legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                                    # third left eat
                                    if row > 1 and col > 1 and (
                                            board[newRow - 1][newCol - 1].startswith("DW") or board[newRow - 1][
                                        newCol - 1].startswith("DWK")) and \
                                            board[newRow - 2][newCol - 2] == "D":
                                        legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                                # second left eat
                                if newRow > 1 and newCol > 1 and (
                                        board[newRow - 1][newCol - 1].startswith("DW") or board[newRow - 1][
                                    newCol - 1].startswith("DWK")) and \
                                        board[newRow - 2][newCol - 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                                    newRow = newRow - 2
                                    newCol = newCol - 2
                                    # third right eat
                                    if newRow > 1 and col < 6 and (
                                            board[newRow - 1][newCol + 1].startswith("DW") or board[newRow - 1][
                                        newCol + 1].startswith("DWK")) and \
                                            board[newRow - 2][newCol + 2] == "D":
                                        legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                                    # third left eat
                                    if newRow > 1 and newCol > 1 and (
                                            board[newRow - 1][newCol - 1].startswith("DW") or board[newRow - 1][
                                        newCol - 1].startswith("DWK")) and \
                                            board[newRow - 2][newCol - 2] == "D":
                                        legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                            # ------------------------------------------------------------------------------------------------
                            # first right eat (Second cond)
                            if row > 1 and col < 6 and (
                                    board[row - 1][col + 1].startswith("DW") or board[row - 1][col + 1].startswith(
                                "DWK")) and board[row - 2][
                                col + 2] == "D":
                                legal_moves.append([(row, col), (row - 2, col + 2)])
                                newRow = row - 2
                                newCol = col + 2
                                # second right eat
                                if newRow > 1 and newCol < 6 and (
                                        board[newRow - 1][newCol + 1].startswith("DW") or board[newRow - 1][
                                    newCol + 1].startswith("DWK")) and \
                                        board[newRow - 2][newCol + 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                                    newRow = newRow - 2
                                    newCol = newCol + 2
                                    # third right eat
                                    if newRow > 1 and newCol < 6 and (
                                            board[newRow - 1][newCol + 1].startswith("DW") or board[newRow - 1][
                                        newCol + 1].startswith("DWK")) and \
                                            board[newRow - 2][newCol + 2] == "D":
                                        legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                                    # third left eat
                                    if newRow > 1 and newCol > 1 and (
                                            board[newRow - 1][newCol - 1].startswith("DW") or board[newRow - 1][
                                        newCol - 1].startswith("DWK")) and \
                                            board[newRow - 2][newCol - 2] == "D":
                                        legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                                # second left eat
                                if newRow > 1 and newCol > 1 and (
                                        board[newRow - 1][newCol - 1].startswith("DW") or board[newRow - 1][
                                    newCol - 1].startswith("DWK")) and \
                                        board[newRow - 2][newCol - 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                                    newRow = newRow - 2
                                    newCol = newCol - 2
                                    # third right eat
                                    if newRow > 1 and newCol < 6 and (
                                            board[newRow - 1][newCol + 1].startswith("DW") or board[newRow - 1][
                                        newCol + 1].startswith("DWK")) and \
                                            board[newRow - 2][newCol + 2] == "D":
                                        legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                                    # third left eat
                                    if newRow > 1 and newCol > 1 and (
                                            board[newRow - 1][newCol - 1].startswith("DW") or board[newRow - 1][
                                        newCol - 1].startswith("DWK")) and \
                                            board[newRow - 2][newCol - 2] == "D":
                                        legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                            # Dark King moves
                            # -----------------------------------------------------------------------------------------

                    # Diagonal jumps
                    if row < 7 and col > 0 and board[row + 1][col - 1] == "D":
                        legal_moves.append([(row, col), (row + 1, col - 1)])
                    if row < 7 and col < 7 and board[row + 1][col + 1] == "D":
                        legal_moves.append([(row, col), (row + 1, col + 1)])
                    # Diagonal jumps

                    # Multiple jumps
                    # first left eat (First cond)
                    if row < 6 and col > 1 and (board[row + 1][col - 1].startswith("DW") or board[row + 1][col - 1].startswith("DWK")) and board[row + 2][col - 2] == "D":
                        legal_moves.append(((row, col), (row + 2, col - 2)))
                        newRow = row + 2
                        newCol = col - 2
                        # second right eat
                        if newRow < 6 and newCol < 6 and (board[newRow + 1][newCol + 1].startswith("DW") or board[newRow + 1][newCol + 1].startswith("DWK")) and \
                                board[newRow + 2][newCol + 2] == "D":
                            legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                            newRow = newRow + 2
                            newCol = newCol + 2
                            # third right eat
                            if newRow < 6 and newCol < 6 and (
                                    board[newRow + 1][newCol + 1].startswith("DW") or board[newRow + 1][
                                newCol + 1].startswith("DWK")) and \
                                    board[newRow + 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                            # third left eat
                            if newRow < 6 and newCol > 1 and (board[newRow + 1][newCol - 1].startswith("DW") or board[newRow + 1][newCol - 1].startswith("DWK")) and \
                                    board[newRow + 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                        # second left eat
                        if newRow < 6 and newCol > 1 and (board[newRow + 1][newCol - 1].startswith("DW") or board[newRow + 1][newCol - 1].startswith("DWK")) and \
                                board[newRow + 2][newCol - 2] == "D":
                            legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                            newRow = newRow + 2
                            newCol = newCol - 2
                            # third right eat
                            if newRow < 6 and col < 6 and (
                                    board[newRow + 1][newCol + 1].startswith("DW") or board[newRow + 1][
                                newCol - 1].startswith("DWK")) and \
                                    board[newRow + 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                            # third left eat
                            if newRow < 6 and newCol > 1 and (
                                    board[newRow + 1][newCol - 1].startswith("DW") or board[newRow + 1][
                                newCol - 1].startswith("DWK")) and \
                                    board[newRow - 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                    # ------------------------------------------------------------------------------------------------
                    # first right eat (Second cond)
                    if row < 6 and col < 6 and (
                            board[row + 1][col + 1].startswith("DW") or board[row + 1][col + 1].startswith("DWK")) and \
                            board[row + 2][
                                col + 2] == "D":
                        legal_moves.append([(row, col), (row + 2, col + 2)])
                        newRow = row + 2
                        newCol = col + 2
                        # second right eat
                        if newRow < 6 and newCol < 6 and (
                                board[newRow + 1][newCol + 1].startswith("DW") or board[newRow + 1][
                            newCol + 1].startswith("DWK")) and \
                                board[newRow + 2][newCol + 2] == "D":
                            legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                            newRow = newRow + 2
                            newCol = newCol + 2
                            # third right eat
                            if newRow < 6 and newCol < 6 and (
                                    board[newRow + 1][newCol + 1].startswith("DW") or board[newRow + 1][
                                newCol + 1].startswith("DWK")) and \
                                    board[newRow + 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                            # third left eat
                            if newRow < 6 and newCol > 1 and (
                                    board[newRow + 1][newCol - 1].startswith("DW") or board[newRow + 1][
                                newCol - 1].startswith("DWK")) and \
                                    board[newRow + 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                        # second left eat
                        if newRow < 6 and newCol > 1 and (
                                board[newRow + 1][newCol - 1].startswith("DW") or board[newRow + 1][
                            newCol - 1].startswith("DWK")) and \
                                board[newRow + 2][newCol - 2] == "D":
                            legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                            newRow = newRow + 2
                            newCol = newCol - 2
                            # third right eat
                            if newRow < 6 and newCol < 6 and (
                                    board[newRow + 1][newCol + 1].startswith("DW") or board[newRow + 1][
                                newCol + 1].startswith("DWK")) and \
                                    board[newRow + 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                            # third left eat
                            if newRow < 6 and newCol > 1 and (
                                    board[newRow + 1][newCol - 1].startswith("DW") or board[newRow + 1][
                                newCol - 1].startswith("DWK")) and \
                                    board[newRow - 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                                # multiple jumps
                elif player == "DW":
                    if board[row][col] == player + 'K':
                        # White King moves
                        # -----------------------------------------------------------------------------------------
                        # first left eat (First cond)
                        if row < 7 and col > 0 and board[row + 1][col - 1] == "D":
                            legal_moves.append([(row, col), (row + 1, col - 1)])
                        if row < 7 and col < 7 and board[row + 1][col + 1] == "D":
                            legal_moves.append([(row, col), (row + 1, col + 1)])
                        if row < 6 and col > 1 and (
                                board[row + 1][col - 1].startswith("DD") or board[row + 1][col - 1].startswith(
                            "DDK")) and board[row + 2][col - 2] == "D":
                            legal_moves.append(((row, col), (row + 2, col - 2)))
                            newRow = row + 2
                            newCol = col - 2
                            # second right eat
                            if newRow < 6 and newCol < 6 and (
                                    board[newRow + 1][newCol + 1].startswith("DD") or board[newRow + 1][
                                newCol + 1].startswith("DDK")) and \
                                    board[newRow + 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                                newRow = newRow + 2
                                newCol = newCol + 2
                                # third right eat
                                if row < 6 and col < 6 and (
                                        board[newRow + 1][newCol + 1].startswith("DD") or board[newRow + 1][
                                    newCol + 1].startswith("DDK")) and \
                                        board[newRow + 2][newCol + 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                                # third left eat
                                if row < 6 and col > 1 and (
                                        board[newRow + 1][newCol - 1].startswith("DD") or board[newRow + 1][
                                    newCol - 1].startswith("DDK")) and \
                                        board[newRow + 2][newCol - 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                            # second left eat
                            if newRow < 6  and newCol > 1 and (
                                    board[newRow + 1][newCol - 1].startswith("DD") or board[newRow + 1][
                                newCol - 1].startswith("DDK")) and \
                                    board[newRow + 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                                newRow = newRow + 2
                                newCol = newCol - 2
                                # third right eat
                                if newRow < 6 and col < 6 and (
                                        board[newRow + 1][newCol + 1].startswith("DD") or board[newRow + 1][
                                    newCol + 1].startswith("DDK")) and \
                                        board[newRow + 2][newCol + 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                                # third left eat
                                if newRow < 6 and newCol > 1 and (board[newRow + 1][newCol - 1].startswith(
                                        "DD") or board[newRow + 1][newCol - 1].startswith("DDK")) and \
                                        board[newRow - 2][newCol - 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                        # ------------------------------------------------------------------------------------------------
                        # first right eat (Second cond)
                        if row < 6 and col < 6 and (
                                board[row + 1][col + 1].startswith("DD") or board[row + 1][col + 1].startswith(
                            "DDK")) and board[row + 2][
                            col + 2] == "D":
                            legal_moves.append([(row, col), (row + 2, col + 2)])
                            newRow = row + 2
                            newCol = col + 2
                            # second right eat
                            if newRow < 6 and newCol < 6 and (
                                    board[newRow + 1][newCol + 1].startswith("DD") or board[newRow + 1][
                                newCol + 1].startswith("DDK")) and \
                                    board[newRow + 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                                newRow = newRow + 2
                                newCol = newCol + 2
                                # third right eat
                                if newRow < 6 and newCol < 6 and (
                                        board[newRow + 1][newCol + 1].startswith("DD") or board[newRow + 1][
                                    newCol + 1].startswith("DDK")) and \
                                        board[newRow + 2][newCol + 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                                # third left eat
                                if newRow < 6 and newCol > 1 and (
                                        board[newRow + 1][newCol - 1].startswith("DD") or board[newRow + 1][
                                    newCol - 1].startswith("DDK")) and \
                                        board[newRow + 2][newCol - 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                            # second left eat
                            if newRow < 6 and newCol > 1 and (
                                    board[newRow + 1][newCol - 1].startswith("DD") or board[newRow + 1][
                                newCol - 1].startswith("DDK")) and \
                                    board[newRow + 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                                newRow = newRow + 2
                                newCol = newCol - 2
                                # third right eat
                                if newRow < 6 and newCol < 6 and (
                                        board[newRow + 1][newCol + 1].startswith("DD") or board[newRow + 1][
                                    newCol + 1].startswith("DDK")) and \
                                        board[newRow + 2][newCol + 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                                # third left eat
                                if newRow < 6 and newCol > 1 and (
                                        board[newRow + 1][newCol - 1].startswith("DD") or board[newRow + 1][
                                    newCol - 1].startswith("DDK")) and \
                                        board[newRow - 2][newCol - 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                        # White King moves -----------------------------------------------------------------------------------------

                    # Digonal moves
                    if row > 0 and col > 0 and board[row - 1][col - 1] == "D":
                        legal_moves.append([(row, col), (row - 1, col - 1)])
                    if row > 0 and col < 7 and board[row - 1][col + 1] == "D":
                        legal_moves.append([(row, col), (row - 1, col + 1)])
                        # Digonal moves
                        # multiple jumps

                        # first left eat(First cond)
                    if row > 1 and col > 1 and (
                            board[row - 1][col - 1].startswith("DD") or board[row - 1][col - 1].startswith("DDK")) and \
                            board[row - 2][
                                col - 2] == "D":
                        legal_moves.append([(row, col), (row - 2, col - 2)])
                        newRow = row - 2
                        newCol = col - 2
                        # second right eat
                        if newRow > 1 and newCol < 6 and (
                                board[newRow - 1][newCol + 1].startswith("DD") or board[newRow - 1][
                            newCol + 1].startswith("DDK")) and \
                                board[newRow - 2][newCol + 2] == "D":
                            legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                            newRow = newRow - 2
                            newCol = newCol + 2
                            # third right eat
                            if row > 1 and col < 6 and (
                                    board[newRow - 1][newCol + 1].startswith("DD") or board[newRow - 1][
                                newCol + 1].startswith("DDK")) and \
                                    board[newRow - 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                            # third left eat
                            if row > 1 and col > 1 and (
                                    board[newRow - 1][newCol - 1].startswith("DD") or board[newRow - 1][
                                newCol - 1].startswith("DDK")) and \
                                    board[newRow - 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                        # second left eat
                        if newRow > 1 and newCol > 1 and (
                                board[newRow - 1][newCol - 1].startswith("DD") or board[newRow - 1][
                            newCol - 1].startswith("DDK")) and \
                                board[newRow - 2][newCol - 2] == "D":
                            legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                            newRow = newRow - 2
                            newCol = newCol - 2
                            # third right eat
                            if newRow > 1 and col < 6 and (
                                    board[newRow - 1][newCol + 1].startswith("DD") or board[newRow - 1][
                                newCol + 1].startswith("DDK")) and \
                                    board[newRow - 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                            # third left eat
                            if newRow > 1 and newCol > 1 and (
                                    board[newRow - 1][newCol - 1].startswith("DD") or board[newRow - 1][
                                newCol - 1].startswith("DDK")) and \
                                    board[newRow - 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                    # ------------------------------------------------------------------------------------------------
                    # first right eat (Second cond)
                    if row > 1 and col < 6 and (
                            board[row - 1][col + 1].startswith("DD") or board[row - 1][col + 1].startswith("DDK")) and \
                            board[row - 2][
                                col + 2] == "D":
                        legal_moves.append([(row, col), (row - 2, col + 2)])
                        newRow = row - 2
                        newCol = col + 2
                        # second right eat
                        if newRow > 1 and newCol < 6 and (
                                board[newRow - 1][newCol + 1].startswith("DD") or board[newRow - 1][
                            newCol + 1].startswith("DDK")) and \
                                board[newRow - 2][newCol + 2] == "D":
                            legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                            newRow = newRow - 2
                            newCol = newCol + 2
                            # third right eat
                            if newRow > 1 and newCol < 6 and (
                                    board[newRow - 1][newCol + 1].startswith("DD") or board[newRow - 1][
                                newCol + 1].startswith("DDK")) and \
                                    board[newRow - 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                            # third left eat
                            if newRow > 1 and newCol > 1 and (
                                    board[newRow - 1][newCol - 1].startswith("DD") or board[newRow - 1][
                                newCol - 1].startswith("DDK")) and \
                                    board[newRow - 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                        # second left eat
                        if newRow > 1 and newCol > 1 and (
                                board[newRow - 1][newCol - 1].startswith("DD") or board[newRow - 1][
                            newCol - 1].startswith("DDK")) and \
                                board[newRow - 2][newCol - 2] == "D":
                            legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                            newRow = newRow - 2
                            newCol = newCol - 2
                            # third right eat
                            if newRow > 1 and newCol < 6 and (
                                    board[newRow - 1][newCol + 1].startswith("DD") or board[newRow - 1][
                                newCol + 1].startswith("DDK")) and \
                                    board[newRow - 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                            # third left eat
                            if newRow > 1 and newCol > 1 and (
                                    board[newRow - 1][newCol - 1].startswith("DD") or board[newRow - 1][
                                newCol - 1].startswith("DDK")) and \
                                    board[newRow - 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                                # multiple jumps
                                # check for valid diagonal moves

    return legal_moves


import copy


def evaluate(board, player,selected_strategy):
    DarkPieces = sum(row.count("DD") + row.count("DDK") for row in board)
    WhitePieces = sum(row.count("DW") + row.count("DWK") for row in board)
    DarkKings = sum(row.count("DDK") for row in board)
    WhiteKings = sum(row.count("DWK") for row in board)
    WhiteMoves = len(small_legal_moves(board, "DW"))
    DarkMoves = len(small_legal_moves(board, "DD"))
    # score = (DarkPieces - WhitePieces)
    # if player == "DW" and WhiteKings < 3:
    #     score += (DarkKings - WhiteKings)
    # else:
    #     score += (DarkKings * 0.5 - WhiteKings * 0.5)
    # for row in board[0]:
    #     if row == "DWK":
    #         score += 1
    # score += (DarkMoves - WhiteMoves) * 0.1
    # return score
    if selected_strategy == "Attack":
        score = (DarkPieces - WhitePieces)
        score += (DarkKings * 0.1 - WhiteKings * 0.1)
        score += (DarkMoves - WhiteMoves) * 0.2
        return score
    elif selected_strategy == "Plot" :
        score = (DarkPieces - WhitePieces)
        if WhiteKings < 3:
            score += (DarkKings - WhiteKings)
        else:
            score += (DarkKings * 0.5 - WhiteKings * 0.5)
        for row in board[0]:
            if row == "DWK":
                score += 1
        score += (DarkMoves - WhiteMoves) * 0.1
        return score


def minimax(board, player, depth, max_player,selected_strategy):
    next_player = "DD" if player == "DW" else "DW"

    if depth == 0 or winner(board,0):
        result = evaluate(board, player,selected_strategy)
        new_board = copy.deepcopy(board)
        return result, [],selected_strategy

    if not max_player:
        min_value = float('inf')
        for move in small_legal_moves(board, player):
            new_board = copy.deepcopy(board)
            White_legal_moves = small_legal_moves(new_board, player)
            piece, new_place = move
            if len(White_legal_moves) == 0:
                winner(board,0)
            else:
                new_board = moveHuman(new_board, piece, new_place, player,0)
                value, new_move,selected_strategy = minimax(new_board, next_player, depth - 1, True,selected_strategy)
                min_value = min(min_value, value)
                if value <= min_value:
                    best_move = move
    else:
        max_value = -float('inf')
        for move in small_legal_moves(board, next_player):
            new_board = copy.deepcopy(board)
            legal_moves = small_legal_moves(new_board, next_player)
            if len(legal_moves) == 0:
                winner(board,0)
            else:
                Computer(board, "DD",0)
            value, new_move,selected_strategy = minimax(new_board, player, depth - 1, False,selected_strategy)
            max_value = max(max_value, value)
            if value >= max_value:
                best_move = move
    return value, best_move,selected_strategy


def play_ai_move(board, player, depth,selected_strategy):
    value, best_move,selected_strategy = minimax(board, player, depth, False,selected_strategy)
    if best_move is not None:
        moveHuman(board, best_move[0], best_move[1], player)
    return board

def Alpha_beta_pruning(board, player, depth, alpha, beta, max_player, selected_strategy):
    next_player = "DD" if player == "DW" else "DW"

    if depth == 0 or winner(board, 0):
        result = evaluate(board, player, selected_strategy)
        new_board = copy.deepcopy(board)
        return result, [], selected_strategy

    if not max_player:
        min_value = float('inf')
        best_move = None
        for move in small_legal_moves(board, player):
            new_board = copy.deepcopy(board)
            White_legal_moves = small_legal_moves(new_board, player)
            piece, new_place = move
            if len(White_legal_moves) == 0:
                winner(board, 0)
            else:
                new_board = moveHuman(new_board, piece, new_place, player,0)
                value, new_move, selected_strategy = Alpha_beta_pruning(
                    new_board, next_player, depth - 1, alpha, beta, True, selected_strategy
                )
                if value <= min_value:
                    min_value = value
                    best_move = move
                beta = min(beta, min_value)
                if alpha >= beta:
                    break  # Beta cutoff
        return min_value, best_move, selected_strategy
    else:
        max_value = -float('inf')
        best_move = None
        for move in small_legal_moves(board, next_player):
            new_board = copy.deepcopy(board)
            legal_moves = small_legal_moves(new_board, next_player)
            if len(legal_moves) == 0:
                winner(board, 0)
            else:
                Computer(board, "DD",0)
            value, new_move, selected_strategy = Alpha_beta_pruning(
                new_board, player, depth - 1, alpha, beta, False, selected_strategy
            )
            if value >= max_value:
                max_value = value
                best_move = move
            alpha = max(alpha, max_value)
            if alpha >= beta:
                break  # Alpha cutoff
        return max_value, best_move, selected_strategy



def play_alpha_beta_ai(board, player, depth,selected_strategy):
    value, best_move,selected_strategy = Alpha_beta_pruning(board, player, depth, -float('inf'), float('inf'), False,selected_strategy)
    if best_move is not None:
        moveHuman(board, best_move[0], best_move[1], player,1)
    return board

def moveHuman(board, piece, new_place, player,realplay):
    DarkPieces = sum(row.count("DD") + row.count("DDK") for row in board)
    WhitePieces = sum(row.count("DW") + row.count("DWK") for row in board)
    DarkKings = sum(row.count("DDK") for row in board)
    WhiteKings = sum(row.count("DWK") for row in board)
    moved = False
    moves = get_legal_moves(board, player)
    Temp = (0, 0)
    for move in moves:
        if Temp == move[0]:
            mid_row = (move[0][0] + move[1][0]) // 2
            mid_col = (move[0][1] + move[1][1]) // 2

            # remove the piece that is being jumped
            if board[mid_row][mid_col].startswith("DD"):
                DarkPieces -= 1
            elif board[mid_row][mid_col].startswith("DW"):
                WhitePieces -= 1
            board[mid_row][mid_col] = "D"

            # move the piece to the new place
            board[move[1][0]][move[1][1]] = board[move[0][0]][move[0][1]]
            board[move[0][0]][move[0][1]] = "D"
            # promote the piece to a king if it reaches the end row
            if player == "DW" and move[1][0] == 0 and board[move[1][0]][move[1][1]] == "DW":
                board[move[1][0]][move[1][1]] = "DWK"
                WhiteKings += 1
            elif player == "DD" and move[1][0] == 7 and board[move[1][0]][move[1][1]] == "DD":
                board[move[1][0]][move[1][1]] = "DDK"
                DarkKings += 1
            if realplay == 1:
                start_gui(board)
                time.sleep(2)
            Temp = move[1]
            moved = True
        if move[0] == piece and move[1] == new_place:
            X, Y = piece[0], piece[1]

            # check if the move is a jump
            if abs(move[1][0] - piece[0]) == 2:
                mid_row = (move[0][0] + move[1][0]) // 2
                mid_col = (move[0][1] + move[1][1]) // 2

                # remove the piece that is being jumped
                if board[mid_row][mid_col].startswith("DD"):
                    DarkPieces -= 1
                elif board[mid_row][mid_col].startswith("DW"):
                    WhitePieces -= 1
                elif board[mid_row][mid_col].startswith("DWK"):
                    WhitePieces -= 1
                    WhiteKings -= 1
                elif board[mid_row][mid_col].startswith("DDK"):
                    DarkPieces -= 1
                    DarkKings -= 1
                board[mid_row][mid_col] = "D"

            # move the piece to the new place
            board[move[1][0]][move[1][1]] = board[move[0][0]][move[0][1]]
            board[move[0][0]][move[0][1]] = "D"

            # promote the piece to a king if it reaches the end row
            if player == "DW" and move[1][0] == 0 and board[move[1][0]][move[1][1]] == "DW":
                board[move[1][0]][move[1][1]] = "DWK"
                WhiteKings += 1
            elif player == "DD" and move[1][0] == 7 and board[move[1][0]][move[1][1]] == "DD":
                board[move[1][0]][move[1][1]] = "DDK"
                DarkKings += 1
            if realplay == 1:
                start_gui(board)
                time.sleep(2)
            Temp = move[1]
            moved = True
    if moved == False:
        print("That's an illegal move!")
    return board


def Print_board(board):
    # Print the header row with column indices
    print("   ", end="")
    for i in range(len(board[0])):
        print(f"{i:2d} ", end="")
    print()

    # Print the board elements with row indices
    for i, row in enumerate(board):
        print(f"{i:2d} ", end="")
        for element in row:
            print(f"{element:2s} ", end="")
        print()


def Computer(board, player,RealPlay):
    legal_moves = small_legal_moves(board, player)
    if len(legal_moves) == 0:
        winner(board,0)
    else:
        choice = random.choice(legal_moves)
        moveHuman(board, choice[0], choice[1], player,RealPlay)

import tkinter.messagebox as messagebox
def winner(new_board,FromMain):
    DarkPieces = sum(row.count("DD") + row.count("DDK") for row in board)
    WhitePieces = sum(row.count("DW") + row.count("DWK") for row in board)
    if (WhitePieces == 0):
        if FromMain==1:
            messagebox.showinfo("Game Over", "Winner is Black pieces, ate all the white pieces!")
        return True
    elif (DarkPieces == 0):
        if FromMain==1:
            messagebox.showinfo("Game Over","Winner is White pieces, ate all the Black pieces!")
        return True
    elif (not small_legal_moves(new_board, "DW")):
        if FromMain==1:
            messagebox.showinfo("Game Over","Winner is Dark pieces, no available moves for White pieces!")
        return True
    elif (not small_legal_moves(new_board, "DD")):
        if FromMain==1:
            messagebox.showinfo("Game Over","Winner is White pieces, no available moves for Dark pieces!")
        return True
    else:
        return False


if __name__ == "__main__":
    selected_level, selected_strategy, selected_algorithm = level_selection()
    print("Selected level:", selected_level)
    print("Selected strategy:", selected_strategy)
    print("Selected algorithm:", selected_algorithm)
    if selected_level == 1:
        depth = 2
    elif selected_level == 2:
        depth = 4
    elif selected_level == 3:
        depth = 6
    counter = 0
    DarkPieces = 12
    WhitePieces = 12
    WhiteKings = 0
    DarkKings = 0
    board = create_board()
    start_gui(board)
    time.sleep(1)
    start_time = time.time()
    while not winner(board,1) == True:
        if counter % 2 == 0:
            player = "DW"
            if selected_algorithm == "Minimax":
                play_ai_move(board, player, depth,selected_strategy)
            elif selected_algorithm == "Alpha":
                play_alpha_beta_ai(board,player,depth,selected_strategy)
        elif not counter % 2 == 0:
            player = "DD"
            Computer(board, player,1)
        counter += 1
end_time = time.time()
time.sleep(1)
elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time} seconds")

