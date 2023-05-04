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
        while (True):
            bomb_location = input("Type where you would like to place your bomb (e.g. A1): ")
            print(bomb_location)
            if (Game.validate_bomb_deployment(bomb_location)):
                print(f'Approved. The bomb will now be deployed.')
                # Go to handle_bomb_deployment.
                return
            else:
                print("Please try again.")
                print("")
    
    def validate_bomb_deployment(bomb):
        stripped_bomb = bomb.replace(" ", "")
        print(f'original input: {bomb}')
        print(f"stripped input: {stripped_bomb}")

        if (len(stripped_bomb) != 2):
            print(f'Invalid input. String must be 2 characters long.')
            return False

        if (stripped_bomb[0].isalpha() == False):
            print(f'Invalid input. The first character must be a letter ranging from A to F.')
            return False

        s = stripped_bomb[0].upper()
        if (s != 'A' or s != 'B' or s != 'C' or s != 'D' or s != 'E' or s != 'F'):
            print(f'Invalid input. The first character must be a letter ranging from A to F.')
            return False

        if (stripped_bomb[1].isnumeric() == False):
            print(f'Invalid input. The second character must be a number between 1 and 6.')
            return False

        # I could also check to see if the user has already deployed a bomb at that location but that's a skill issue imo.
        
        else:
            return True

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

    board = [
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
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