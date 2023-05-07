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
    Board = [["W", "DD", "W", "DD", "W", "DD", "W", "DD"],
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
                    if row < 6 and col > 1 and board[row + 1][col - 1].startswith("DW") and board[row + 2][
                        col - 2] == "D":
                        legal_moves.append(((row, col), (row + 2, col - 2)))
                    if row < 6 and col < 6 and board[row + 1][col + 1].startswith("DW") and board[row + 2][
                        col + 2] == "D":
                        legal_moves.append([(row, col), (row + 2, col + 2)])
                elif player == "DW":
                    if row > 0 and col > 0 and board[row - 1][col - 1] == "D":
                        legal_moves.append([(row, col), (row - 1, col - 1)])
                    if row > 0 and col < 7 and board[row - 1][col + 1] == "D":
                        legal_moves.append([(row, col), (row - 1, col + 1)])
                    if row > 1 and col > 1 and board[row - 1][col - 1].startswith("DD") and board[row - 2][
                        col - 2] == "D":
                        legal_moves.append([(row, col), (row - 2, col - 2)])
                    if row > 1 and col < 6 and board[row - 1][col + 1].startswith("DD") and board[row - 2][
                        col + 2] == "D":
                        legal_moves.append([(row, col), (row - 2, col + 2)])
    return legal_moves

def Print_board():
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


def moveHuman(piece, NewPlace,player):
    Moves = get_legal_moves(board,player)
    Print_board()
    found=False
    for lst in Moves:
        Temp = lst
        if lst[0] == piece and lst[1] == NewPlace:
            first_tuple = Temp[0]
            X = first_tuple[0]
            Y=first_tuple[1]
            Second_tuple = Temp[1]
            X2 = Second_tuple[0]
            Y2 = Second_tuple[1]
            board[X][Y]="D"
            board[X2][Y2]=player
            print(Moves)
            Print_board()
            found=True
    if found==False:
        print("That's an illegal move")

# def winner():
#     for i


board = create_board()
print(get_legal_moves(board,"DW"))
#moveHuman((5, 0),(4, 0),"DW")


if __name__ == "__main__":
    board = create_board()
