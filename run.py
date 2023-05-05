# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import sys

class Game:
    def run_game():
        # Initialise the game.
        user = Board("user")
        user.print_board()
        comp = Board("comp")
        comp.print_board()
        Game.main_game_loop(user, comp)
        return

    def main_game_loop(user, comp):
        # The main game loop runs here. Only exits with winning condition.
        while True:
            bomb = Game.ask_user_to_deploy_bombs(user, comp)
            Game.handle_bomb_deployment(user, comp, bomb)
            if (user.check_win_condition()):
                Game.ask_if_user_wishes_to_play_again(user, comp)
            Game.comp_makes_a_move(user, comp)
            if (comp.check_win_condition()):
                Game.ask_if_user_wishes_to_play_again(user, comp)
    
    def ask_user_to_deploy_bombs(user, comp):
        # Ask user for input.
        while (True):
            bomb_location = input("Type where you would like to place your bomb (e.g. A1): ")
            print(bomb_location)
            stripped_bomb = bomb_location.replace(" ", "")
            if (Game.validate_bomb_deployment(stripped_bomb)):
                print(f'Approved. The bomb will now be deployed.')
                # Go to handle_bomb_deployment.
                return stripped_bomb
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

    def handle_bomb_deployment(user, comp, bomb):
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

    def comp_makes_a_move(user, comp):
        # Computer to do a move.
        print("The computer will now make their move.")
        while True:
            i = random.randint(0, 5)
            j = random.randint(0, 5)
            if (comp.board[j][i] == "X"):
                continue
            else:
                print(f'Computer deploying bomb at ({i}, {j})')
            if (comp.board[j][i] == "*"):
                print("It's a hit!")
            else:
                print("Computer bomb landed in water.")
            comp.board[j][i] = "X"
            return
    
    def ask_if_user_wishes_to_play_again(user, comp):
        # Ask user if they wish to play the game again.
        while True:
            play_again = input("Would you like to play again? (y/n): ")
            if (play_again == "y"):
                user.generate_game_board()
                comp.generate_game_board()
                Game.run_game()
            elif (play_again == "n"):
                print("I hope you had fun playing!")
                print("Now closing program...")
                sys.exit()
            else:
                print("Invalid input, please try again.")
        return
    


class Board:

    def __init__(self, name):
        self.name = name

    board = [
        ["*", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", "*", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "]
    ]

    def generate_game_board(self):
        self.board = [
        ["*", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", "*", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "]
    ]

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
            print("There is still more fun to be had.")
            return False
        else:
            print(f'Game Over! {self.name} wins!!')
            return True

Game.run_game()