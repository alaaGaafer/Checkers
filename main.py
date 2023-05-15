import sys
import time

import pygame
def start_gui():
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
            pygame.draw.rect(board_surface, color,
                             [col * (board_size / 8), row * (board_size / 8), (board_size / 8), (board_size / 8)])

    # Set the position of the board on the screen
    board_x = (screen_width - board_width) // 2
    board_y = (screen_height - board_height) // 2

    # Load the images for the checkers and scale them down
    DD = pygame.image.load('pics/darkpng.png')
    DW = pygame.image.load('pics/whitepng.png')
    DW = pygame.transform.scale(DW, (int(board_size / 8), int(board_size / 8)))
    DD = pygame.transform.scale(DD, (int(board_size / 8), int(board_size / 8)))

    # Place the checkers on the board
    for row in range(8):
        for col in range(8):
            if board[row][col] == 'DW':
                board_surface.blit(DW, (col * (board_size / 8), row * (board_size / 8)))
            elif board[row][col] == 'DD':
                board_surface.blit(DD, (col * (board_size / 8), row * (board_size / 8)))

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
    Board = [["W", "DD", "W", "DD", "W", "D", "W", "DD"],
             ["D", "W", "D", "W", "DD", "W", "DD", "W"],
             ["W", "DD", "W", "D", "W", "DD", "W", "DD"],
             ["D", "W", "D", "W", "D", "W", "D", "W"],
             ["W", "DD", "W", "D", "W", "D", "W", "D"],
             ["D", "W", "D", "W", "DW", "W", "DW", "W"],
             ["W", "DD", "W", "DW", "W", "DW", "W", "DW"],
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
                        if row > 1 and col > 1 and (board[row - 1][col - 1].startswith("DW") or board[row - 1][col - 1].startswith("DWK")) and board[row - 2][
                            col - 2] == "D":
                            legal_moves.append([(row, col), (row - 2, col - 2)])
                        if row > 1 and col < 6 and (board[row - 1][col + 1].startswith("DW") or board[row - 1][col + 1].startswith("DWK")) and board[row - 2][
                            col + 2] == "D":
                            legal_moves.append([(row, col), (row - 2, col + 2)])
                    # Dark king reverse moves
                    # dark pieces moves
                    if row < 7 and col > 0 and board[row + 1][col - 1] == "D":
                        legal_moves.append([(row, col), (row + 1, col - 1)])
                    if row < 7 and col < 7 and board[row + 1][col + 1] == "D":
                        legal_moves.append([(row, col), (row + 1, col + 1)])
                    if row < 6 and col > 1 and (board[row + 1][col - 1].startswith("DW") or board[row + 1][col - 1].startswith("DWK")) and board[row + 2][col - 2] == "D":
                        legal_moves.append(((row, col), (row + 2, col - 2)))
                    if row < 6 and col < 6 and (board[row + 1][col + 1].startswith("DW") or board[row + 1][col + 1].startswith("DWK")) and board[row + 2][col + 2] == "D":
                        legal_moves.append([(row, col), (row + 2, col + 2)])
                    # dark pieces moves
                elif player == "DW":
                    # White king reverse moves
                    if board[row][col] == player + 'K':
                        if row < 7 and col > 0 and board[row + 1][col - 1] == "D":
                            legal_moves.append([(row, col), (row + 1, col - 1)])
                        if row < 7 and col < 7 and board[row + 1][col + 1] == "D":
                            legal_moves.append([(row, col), (row + 1, col + 1)])
                        if row < 6 and col > 1 and (board[row + 1][col - 1].startswith("DD") or board[row + 1][col - 1].startswith("DDK")) and board[row + 2][col - 2] == "D":
                            legal_moves.append(((row, col), (row + 2, col - 2)))
                        if row < 6 and col < 6 and (board[row + 1][col + 1].startswith("DD") or board[row + 1][col + 1].startswith("DDK")) and board[row + 2][col + 2] == "D":
                            legal_moves.append([(row, col), (row + 2, col + 2)])
                    # White king reverse moves
                    # White pieces moves
                    if row > 0 and col > 0 and board[row - 1][col - 1] == "D":
                        legal_moves.append([(row, col), (row - 1, col - 1)])
                    if row > 0 and col < 7 and board[row - 1][col + 1] == "D":
                        legal_moves.append([(row, col), (row - 1, col + 1)])
                    if row > 1 and col > 1 and (board[row - 1][col - 1].startswith("DD") or board[row - 1][col - 1].startswith("DDK")) and board[row - 2][col - 2] == "D":
                        legal_moves.append([(row, col), (row - 2, col - 2)])
                    if row > 1 and col < 6 and (board[row - 1][col + 1].startswith("DD") or board[row - 1][col + 1].startswith("DDK")) and board[row - 2][col + 2] == "D":
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


def moveHuman(board, piece, new_place, player):
    global DarkPieces
    global WhitePieces
    global DarkKings
    global WhiteKings
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
                print("You ate a dark piece!")
            elif board[mid_row][mid_col].startswith("DW"):
                WhitePieces -= 1
                print("You ate a White piece!")
            board[mid_row][mid_col] = "D"

            # move the piece to the new place
            board[move[1][0]][move[1][1]] = board[move[0][0]][move[0][1]]
            board[move[0][0]][move[0][1]] = "D"
            # promote the piece to a king if it reaches the end row
            if player == "DW" and move[1][0] == 0 and board[move[1][0]][move[1][1]] == "DW":
                board[move[1][0]][move[1][1]] = "DWK"
                WhiteKings += 1
                print("The piece was promoted to a king!")
            elif player == "DD" and move[1][0] == 7 and board[move[1][0]][move[1][1]] == "DD":
                board[move[1][0]][move[1][1]] = "DDK"
                DarkKings += 1
                print("The piece was promoted to a king!")
            start_gui()
            time.sleep(3)
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
                    print("You ate a dark piece!")
                elif board[mid_row][mid_col].startswith("DW"):
                    WhitePieces -= 1
                    print("You ate a White piece!")
                elif board[mid_row][mid_col].startswith("DWK"):
                    WhitePieces -= 1
                    WhiteKings-=1
                    print("You ate a White King piece!")
                elif board[mid_row][mid_col].startswith("DDK"):
                    DarkPieces -= 1
                    DarkKings -= 1
                    print("You ate a Dark King piece!")
                board[mid_row][mid_col] = "D"

            # move the piece to the new place
            board[move[1][0]][move[1][1]] = board[move[0][0]][move[0][1]]
            board[move[0][0]][move[0][1]] = "D"

            # promote the piece to a king if it reaches the end row
            if player == "DW" and move[1][0] == 0 and board[move[1][0]][move[1][1]]=="DW":
                board[move[1][0]][move[1][1]] = "DWK"
                WhiteKings += 1
                print("The piece was promoted to a king!")
            elif player == "DD" and move[1][0] == 7 and board[move[1][0]][move[1][1]]=="DD":
                board[move[1][0]][move[1][1]] = "DDK"
                DarkKings += 1
                print("The piece was promoted to a king!")
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

def Computer(board,player):
    legal_moves = small_legal_moves(board,player)
    choice = random.choice(legal_moves)
    moveHuman(board,choice[0],choice[1],player)

def winner(DarkPieces, WhitePieces):
    if (WhitePieces == 0):
        print("Winner is Dark pieces, ate all the white pieces!")
        return True
    elif (DarkPieces == 0):
        print("Winner is White pieces, ate all the white pieces!")
        return True
    elif (not get_legal_moves(board, "DW")):
        print("Winner is Dark pieces, no available moves for White pieces!")
        return True
    elif (not get_legal_moves(board, "DD")):
        print("Winner is White pieces, no available moves for Dark pieces!")
        return True
    else:
        return False

if __name__ == "__main__":
    counter=1
    DarkPieces = 12
    WhitePieces = 12
    while True:
        if counter==1:
            board = create_board()
            start_gui()
            time.sleep(3)
            print(get_legal_moves(board, "DW"))
            moveHuman(board, (7, 0), (5, 2), "DW")
            Print_board(board)
            counter=2
        elif counter == 2:
            time.sleep(3)
            print(get_legal_moves(board, "DW"))
            moveHuman(board, (5, 4), (4, 3), "DW")
            Print_board(board)
            start_gui()
            counter=3
        else:
            time.sleep(20)
    #board = create_board()
