# Checkers Game AI

This project is a Python implementation of the Checkers game with a computer player playing against an AI opponent. The computer player makes random moves, while the AI player uses either the minimax or alpha-beta pruning algorithm based on user selection. The game allows users to choose between different evaluation criteria for the AI player, specifically "Plot" and "Attack," and offers various difficulty levels.

## Functions

- `level_selection()`: Prompts the user to choose the difficulty level for the AI player. The available options depend on the specific implementation of the game and can range from easy to hard difficulty levels.

- `start_gui()`: Initializes the graphical user interface (GUI) for the game, providing an interactive environment where users can play against the AI.

- `create_board()`: Creates the initial game board, setting up the pieces and their positions for the start of the game.

- `small_legal_moves()`: Returns a list of all possible diagonal moves and single eat moves for a given player. This function does not consider multiple eat moves.

- `get_legal_moves()`: Returns a list of all legal moves, including multiple eat moves, for a given player.

- `evaluate(board, player, selected_strategy)`: Evaluates the current game state and returns a score based on the selected evaluation strategy. The evaluation function takes into account factors such as piece count, king count, available moves, and the selected strategy ("Plot" or "Attack").

- `minimax(board, player, depth, max_player, selected_strategy)`: Implements the minimax algorithm with alpha-beta pruning to determine the best move for the AI player. It recursively searches the game tree, evaluating different moves and selecting the one that maximizes the AI's score while minimizing the opponent's score.

- `play_ai_move(board, player, selected_strategy)`: Makes the AI player choose and execute the best move based on the selected evaluation strategy and difficulty level. It uses either the minimax or alpha-beta pruning algorithm, depending on user selection.

- `Alpha_beta_pruning()`: Implements the alpha-beta pruning optimization technique in the minimax algorithm to reduce unnecessary evaluations and improve the efficiency of the AI player's decision-making process.

- `play_alpha_beta_ai(board, player, selected_strategy)`: Makes the AI player choose and execute the best move using the alpha-beta pruning algorithm. It takes into account the selected evaluation strategy and difficulty level.

- `moveHuman(board, piece, new_place, player)`: Moves the player's piece on the board, updates the board state, and handles the promotion of kings. It also removes the opponent's pieces when they are jumped.

- `Print_board(board)`: Prints the current state of the game board in a visually appealing way, representing the pieces and their positions.

- `Computer(board, player)`: Makes the computer player choose and execute a random move on the board. This function is used as a simple opponent for the AI player.

- `winner(board)`: Checks if a player has won the game based on the current board state. It returns the winning player or None if there is no winner yet.

## Usage

1. Ensure you have Python installed on your machine.

2. Clone the repository:

   ```shell
   git clone https://github.com/alaaGaafer/Checkers.git
   python main.py
   
## Contributing
  Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue.
