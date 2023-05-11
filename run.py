# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import sys
import time

class Game:
    """
    A class to represent the game - Battleships Bonanza.
    
    ...

    Methods
    -------
    run_game():
        Runs the game.
    set_game_boards(user,comp):
        Sets up the game boards for all players.
    main_game_loop(user, comp):
        This is where the main loop of the game resides.
    display_game_boards(user, comp):
        Displays game boards in the terminal.
    ask_user_to_deploy_bombs():
        Asks the user for input and exports a string.
    validate_bomb_deployment(bomb):
        Ensures user input is valid.
    handle_bomb_deployment(user, comp, bomb):
        Converts user input to identify correct element in nested list.
    comp_makes_a_move(user, comp):
        Computer selects a random cell to attack.
    ask_if_user_wishes_to_play_again(user, comp):
        Asks user if they wish to play the game again.
    """
    def run_game():
        # Initialise the game.
        user = Player("User")
        comp = Player("Computer")
        Game.set_game_boards(user, comp)
        return

    def set_game_boards(user, comp):
        user.initialise_player()
        comp.initialise_player()
        Game.main_game_loop(user, comp)

    def main_game_loop(user, comp):
        # The main game loop runs here. Only exits with winning condition.
        while True:
            Game.display_game_boards(user, comp)
            bomb = Game.ask_user_to_deploy_bombs()
            Game.handle_bomb_deployment(user, comp, bomb)
            if (user.check_win_condition(comp)):
                Game.ask_if_user_wishes_to_play_again(user, comp)
            time.sleep(2)
            Game.comp_makes_a_move(user, comp)
            if (comp.check_win_condition(user)):
                Game.ask_if_user_wishes_to_play_again(user, comp)
            time.sleep(2)

    def display_game_boards(user, comp):
        user.print_board()
        #comp.print_board()
    
    def ask_user_to_deploy_bombs():
        # Ask user for input.
        while (True):
            bomb_location = input("Type where you would like to place your bomb (e.g. A1): ")
            stripped_bomb = bomb_location.replace(" ", "")
            if (Game.validate_bomb_deployment(stripped_bomb)):
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

        if (ord(bomb[0].upper()) < 65 or ord(bomb[0].upper()) > 70):
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
        print(f"Approved. The bomb will now be deployed at {bomb[0].upper()}{bomb[1]}.")
        i = ord(bomb[0].upper()) - 65
        j = int(bomb[1]) - 1
        user.update_game_board(comp, i, j)
        return

    def comp_makes_a_move(user, comp):
        # Computer to do a move.
        computer_move = comp.random_move()
        print(f"Computer deploying at {chr(computer_move[0]+65)}{computer_move[1] + 1}.")
        comp.update_game_board(user, computer_move[0], computer_move[1])
        return
    
    def ask_if_user_wishes_to_play_again(user, comp):
        # Ask user if they wish to play the game again.
        while True:
            play_again = input("Would you like to play again? (y/n): ")
            if (play_again == "y"):
                print("")
                print("New Game!")
                print("")
                Game.set_game_boards(user, comp)
            elif (play_again == "n"):
                print("I hope you had fun playing!")
                print("Now closing program...")
                sys.exit()
            else:
                print("Invalid input, please try again.")
        return
    


class Player:
    def __init__(self, name):
        self.name = name
        self.board = [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "]
        ]
    
    def initialise_player(self):       
        self.deployments = [
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "]
            ]
        
        self.generate_game_board()

    def generate_game_board(self):
        # Section to come up with locations
        locations = []
        while (len(locations) < 6):
            i = random.randint(0, 5)
            j = random.randint(0, 5)
            if ([i, j] in locations):
                continue
            else:
                locations.append([i, j])
        # Section to assign ships
        for j, sub_array in enumerate(self.board):
            for i, element in enumerate(sub_array):
                if ([i, j] in locations):
                    self.board[j][i] = "*"
                else:
                    self.board[j][i] = " "

    def print_board(self):
        print("")
        print(f"{self.name}'s board:      {self.name}'s deployments:")
        print("")
        print("  A B C D E F            A B C D E F")
        for i, row in enumerate(self.board):
            print(f"{str(i + 1)} {' '.join(row)}          {str(i + 1)} {' '.join(self.deployments[i])}")
        print("")
    
    def update_game_board(self, other, i, j):
        if (other.board[j][i] == "X" or other.board[j][i] == "O"):
            print(f"{self.name} has already deployed a bomb at this location")
            print("")
            return
        elif (other.board[j][i] == " "):
            print(f"{self.name} missed.")
            other.board[j][i] = "X"
        elif (other.board[j][i] == "*"):
            print("It's a hit!")
            other.board[j][i] = "O"
        print("")
        self.deployments[j][i] = other.board[j][i]
        return
    
    def random_move(self):
        while True:
            i = random.randint(0, 5)
            j = random.randint(0, 5)
            if (self.deployments[j][i] == "X" or self.deployments[j][i] == "O"):
                continue
            else:
                computer_move = [i, j]
                return computer_move
    
    def check_win_condition(self, other):
        if ("*" in [item for sublist in other.board for item in sublist]):
            return False
        else:
            self.print_board()
            other.print_board()
            print(f'Game Over! {self.name} wins!!')
            return True

Game.run_game()