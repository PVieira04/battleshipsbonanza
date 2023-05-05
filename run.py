# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

class Game:
    def run_game():
        # Initialise the game.
        user = Board("user")
        user.print_board()
        comp = Board("comp")
        Game.main_game_loop(user, comp)
        return

    def main_game_loop(user, comp):
        # The main game loop runs here. Only exits with winning condition.
        Game.ask_user_to_deploy_bombs(user, comp)
        return
    
    def ask_user_to_deploy_bombs(user, comp):
        # Ask user for input.
        while (True):
            bomb_location = input("Type where you would like to place your bomb (e.g. A1): ")
            print(bomb_location)
            stripped_bomb = bomb_location.replace(" ", "")
            if (Game.validate_bomb_deployment(stripped_bomb)):
                print(f'Approved. The bomb will now be deployed.')
                # Go to handle_bomb_deployment.
                Game.handle_bomb_deployment(user, stripped_bomb)
                return
            else:
                print("Please try again.")
                print("")
    
    def validate_bomb_deployment(bomb):
        if (len(bomb) != 2):
            print(f'Invalid input. String must be 2 characters long.')
            return False

        if (bomb[0].isalpha() == False):
            print(f'Invalid input. The first character must be a letter ranging from A to F.')
            return False

        s = bomb[0].upper()
        print(f'variable "s" is {s}')
        if (s != 'A' and s != 'B' and s != 'C' and s != 'D' and s != 'E' and s != 'F'):
            print(f'Invalid input. The first character must be a letter ranging from A to F.')
            return False

        if (bomb[1].isnumeric() == False):
            print(f'Invalid input. The second character must be a number between 1 and 6.')
            return False

        if (int(bomb[1]) < 1 or int(bomb[1]) > 6):
            print(f'Invalid input. The second character must be a number between 1 and 6.')
            return False

        # I could also check to see if the user has already deployed a bomb at that location but that's a skill issue imo.
        
        else:
            return True

    def handle_bomb_deployment(user, bomb):
        # Logic to update comp game board.
        if (bomb[0] == "A" or bomb[0] == "a"):
            i = 0
        if (bomb[0] == "B" or bomb[0] == "b"):
            i = 1
        if (bomb[0] == "C" or bomb[0] == "c"):
            i = 2
        if (bomb[0] == "D" or bomb[0] == "d"):
            i = 3
        if (bomb[0] == "E" or bomb[0] == "e"):
            i = 4
        if (bomb[0] == "F" or bomb[0] == "f"):
            i = 5
        j = int(bomb[1]) - 1
        print(f'The co-ordinates of deployment are: ({i}, {j})')
        user.update_game_board(i, j)
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

    def __init__(self, name):
        self.name = name

    board = [
        ["*", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", "*", " ", " ", " ", " "],
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

    def print_board(self):
        print("  A B C D E F")
        row_num = 1
        for line in self.board:
            print(str(row_num) + " " + " ".join(line))
            row_num += 1
    
    def update_game_board(self, i, j):
        if (self.board[j][i] == "X"):
            print("This cell has already been hit by a bomb.")
            return
        elif (self.board[j][i] == " "):
            print("You missed.")
        elif (self.board[j][i] == "*"):
            print("It's a hit!")
        self.board[j][i] = "X"
        return
    
    def check_win_condition(self):
        if ("*" in [item for sublist in self.board for item in sublist]):
            print("There is more fu nto be had!")
        else:
            print(f'Game Over! {self.name} wins!!')

Game.run_game()