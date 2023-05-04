# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

class Game:
    def run_game():
        # Initialise the game.
        Board.generate_user_board()
        Board.generate_comp_board()
        Game.main_game_loop()
        return

    def main_game_loop():
        # The main game loop runs here. Only exits with winning condition.
        Game.ask_user_to_deploy_bombs()
        return
    
    def ask_user_to_deploy_bombs():
        # Ask user for input.
        bomb_location = input("Type where you would like to place your bomb (e.g. A1): ")
        print(bomb_location)
        return

    def handle_bomb_deployment():
        # Logic to update comp game board.
        return
    
    def check_if_user_wins():
        # Check if user wins the game.
        return

    def comp_makes_a_move():
        # Computer to do a move.
        return

    def check_if_comp_wins():
        # Check if comp wins the game.
        return
    
    def ask_if_user_wishes_to_play_again():
        # Ask user if they wish to play the game again.
        return

class Board:

    user_board = [
        ["*", " ", " ", " ", " ", "*"],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        ["*", " ", " ", " ", " ", "*"]
    ]

    comp_board = [
        [" ", " ", " ", " ", "*", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", "*", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        ["*", " ", " ", "*", " ", " "],
        [" ", " ", " ", " ", " ", " "]
    ]

    def generate_user_board():
        # Create the board here.
        print("User Board:")
        Board.print_board(Board.user_board)
        return
    
    def generate_comp_board():
        # Create the board here.
        print("Computer Board:")
        Board.print_board(Board.comp_board)
        return

    def print_board(board):
        print("  A B C D E F")
        row_num = 1
        for line in board:
            print(str(row_num) + " " + " ".join(line))
            row_num += 1

Game.run_game()