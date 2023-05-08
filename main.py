def create_board():
    # Board = [
    #       0     1     2     3    4     5    6     7
    #     0["W", "DD", "W", "DD", "W", "DD", "W", "DD"],
    #     1["DD", "W", "DD", "W", "DD", "W", "DD", "W"],
    #     2["W", "DD", "W", "D", "W", "DD", "W", "DD"],
    #     3["D", "W", "DD", "W", "D", "W", "D", "W"],
    #     4["W", "DW", "W", "D", "W", "D", "W", "D"],
    #     5["DW", "W", "DW", "W", "DW", "W", "DW", "W"],
    #     6["W", "DW", "W", "DW", "W", "DW", "W", "DW"],
    #     7["DW", "W", "DW", "W", "DW", "W", "DW", "W"]
    # ]
    Board = [["W", "DD", "W", "DD", "W", "D", "W", "DD"],
             ["DD", "W", "DD", "W", "DD", "W", "DD", "W"],
             ["W", "DD", "W", "D", "W", "DD", "W", "DD"],
             ["D", "W", "DD", "W", "D", "W", "D", "W"],
             ["W", "DW", "W", "D", "W", "D", "W", "D"],
             ["DW", "W", "D", "W", "DW", "W", "DW", "W"],
             ["W", "DW", "W", "DW", "W", "DW", "W", "DW"],
             ["DW", "W", "DW", "W", "DW", "W", "DW", "W"]
             ]

    return Board

def get_legal_moves(board, player):
    legal_moves = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == player or board[row][col] == player + "K":
                # check for valid diagonal moves
                if player == "DD":
                    if row < 7 and col > 0 and board[row + 1][col - 1] == "D":
                        legal_moves.append([(row, col), (row + 1, col - 1)])
                    if row < 7 and col < 7 and board[row + 1][col + 1] == "D":
                        legal_moves.append([(row, col), (row + 1, col + 1)])
                    if row < 6 and col > 1 and board[row + 1][col - 1].startswith("DW") and board[row + 2][col - 2] == "D":
                        legal_moves.append(((row, col), (row + 2, col - 2)))
                    if row < 6 and col < 6 and board[row + 1][col + 1].startswith("DW") and board[row + 2][col + 2] == "D":
                        legal_moves.append([(row, col), (row + 2, col + 2)])
                elif player == "DW":
                    if row > 0 and col > 0 and board[row - 1][col - 1] == "D":
                        legal_moves.append([(row, col), (row - 1, col - 1)])
                    if row > 0 and col < 7 and board[row - 1][col + 1] == "D":
                        legal_moves.append([(row, col), (row - 1, col + 1)])
                    if row > 1 and col > 1 and board[row - 1][col - 1].startswith("DD") and board[row - 2][col - 2] == "D":
                        legal_moves.append([(row, col), (row - 2, col - 2)])
                    if row > 1 and col < 6 and board[row - 1][col + 1].startswith("DD") and board[row - 2][col + 2] == "D":
                        legal_moves.append([(row, col), (row - 2, col + 2)])
    return legal_moves

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



def moveHuman(board, piece, new_place, player):
    global DarkPieces
    global WhitePieces

    moves = get_legal_moves(board, player)

    for move in moves:
        if move[0] == piece and move[1] == new_place:
            X, Y = piece[0], piece[1]

            # check if the move is a jump
            if abs(move[1][0] - piece[0]) == 2:
                mid_row = (move[0][0] + move[1][0]) // 2
                mid_col = (move[0][1] + move[1][1]) // 2

                # remove the piece that is being jumped
                if board[mid_row][mid_col].startswith("D"):
                    DarkPieces -= 1
                    print("You ate a dark piece!")
                elif board[mid_row][mid_col].startswith("W"):
                    WhitePieces -= 1
                    print("You ate a White piece!")
                board[mid_row][mid_col] = "D"

            # move the piece to the new place
            board[move[1][0]][move[1][1]] = board[move[0][0]][move[0][1]]
            board[move[0][0]][move[0][1]] = "D"

            # promote the piece to a king if it reaches the end row
            if player == "W" and move[1][0] == 0:
                board[move[1][0]][move[1][1]] = "WK"
                print("The piece was promoted to a king!")
            elif player == "D" and move[1][0] == 7:
                board[move[1][0]][move[1][1]] = "DK"
                print("The piece was promoted to a king!")
            return True
    print("That's an illegal move!")
    return False

def winner(DarkPieces, WhitePieces):
    if (WhitePieces == 0):
        print("Winner is Dark pieces, ate all the white pieces!")
        return True
    elif (WhitePieces == 0):
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



board = create_board()
DarkPieces=12
WhitePieces=12
print(get_legal_moves(board,"DW"))
moveHuman(board,(4,1),(2,3),"DW")

Print_board(board)


if __name__ == "__main__":
    board = create_board()
