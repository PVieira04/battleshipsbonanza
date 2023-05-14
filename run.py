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
    def welcome_to_the_game():
        print("Welcome to Battleships Bonanza!")
        print("")
        print("Developed by Patrick Vieira")
        print("")
        Game.main_menu()
    
    def main_menu():
        print("")
        while True:
            command = input("Type 'play' to play the game or 'exit' to exit: ")
            if command == "play":
                Game.run_game()
            elif command == "exit":
                sys.exit()
            else:
                print("Invalid command. Please try again.")
                print("")

    def run_game():
        # Initialise the game.
        size = Game.ask_user_for_board_size()
        user = Player("User", size)
        comp = Player("Computer", size)
        Game.ask_user_for_random_or_manual_placement_of_battlships(user, comp)
        #Game.set_game_boards(user, comp)
        return

    def ask_user_for_board_size():
        print("")
        print("The following prompt will accept any number between 4 and 9 inclusive.")
        print("This will set the size of the board, for example:")
        print("Entering '4' will set the board to a 4 by 4 square.")
        while True:
            print("")
            try:
                size = int(input("What size of board would you like? "))
                if size not in range(4, 10):
                    raise ValueError("Invalid input. Please enter a number between 4 and 9 inclusive.")
                return size
            except:
                print("Invalid input. Please enter a number between 4 and 9 inclusive.")
    
    def ask_user_for_random_or_manual_placement_of_battlships(user, comp):
        while True:
            print("")
            string = input("Type 'random' for random battleship placement or type 'manual' to place them yourself: ")
            if string == 'random':
                Game.random_placement(user, comp)
            elif string == 'manual':
                Game.manual_placement(user, comp)
            else:
                print("Invalid input, please try again.")
    
    def random_placement(user, comp):
        battleship_locations = user.random_battleship_placement()
        print(f"Battleship Locations: {battleship_locations}")
        Game.set_computer_game_board(user, comp)
    
    def manual_placement(user, comp):
        Game.manual_leviathan_placement(user)
        Game.set_computer_game_board(user, comp)
        
    def manual_leviathan_placement(user):
        print("")
        user.print_board()
        print("")
        # Variable 'positions' is a list of cell names, e.g. ["A1", "B1", ...] etc.
        positions = user.calculate_available_battleship_positions(user.leviathan_len)
        # When printing my variable 'positions', I could use a function to return a string - better readability.
        print(f"The Leviathan's position can start from the following cells: {positions}")
        print("")
        while True:
            leviathan = input("Type the name of the cell you would like your Leviathan to start at: ")
            # Do some check here
            if leviathan not in positions:
                continue
            # If Leviathan is not in available cells: continue
            print("")
            print("The Leviathan can be placed horizontally or vertically from this position.")
            print("Would you like to place it horizontally or vertically?")
            print("")
            while True:
                direction = input("Type 'h' for horizontal or 'v' for vertical: ")
                if direction not in ['h', 'v']:
                    continue
                elif direction == 'h':
                    # Place it horizontally
                    print("Placing Horizontally")
                elif direction == 'v':
                    # Place it vertically
                    print("Placing Vertically")
            user.manual_battleship_placement()
    
    def set_computer_game_board(user, comp):
        print("Setting up Computer Board")
        battleship_locations = comp.random_battleship_placement()
        Game.main_game_loop(user, comp)

    def set_game_boards(user, comp):
        user.generate_game_board()
        comp.generate_game_board()
        Game.main_game_loop(user, comp)

    def main_game_loop(user, comp):
        # The main game loop runs here. Only exits with winning condition.
        while True:
            Game.display_game_boards(user, comp)
            bomb = Game.ask_user_to_deploy_bombs(user)
            Game.handle_bomb_deployment(user, comp, bomb)
            if (user.check_win_condition(comp)):
                Game.ask_if_user_wishes_to_play_again(user, comp)
            #time.sleep(2)
            Game.comp_makes_a_move(user, comp)
            if (comp.check_win_condition(user)):
                Game.ask_if_user_wishes_to_play_again(user, comp)
            #time.sleep(2)

    def display_game_boards(user, comp):
        user.print_board()
        #comp.print_board()
    
    def ask_user_to_deploy_bombs(user):
        # Ask user for input.
        while (True):
            bomb_location = input("Type where you would like to place your bomb (e.g. A1): ")
            stripped_bomb = bomb_location.replace(" ", "")
            if (Game.validate_bomb_deployment(stripped_bomb, user)):
                # Go to handle_bomb_deployment.
                return stripped_bomb
            else:
                print("Please try again.")
                print("")
    
    def validate_bomb_deployment(bomb, user):
        if (len(bomb) != 2):
            print(f'Invalid input. String must be 2 characters long.')
            return False

        if (bomb[0].isalpha() == False):
            print(f'Invalid input. The first character must be a letter ranging from A to F.')
            return False

        if (ord(bomb[0].upper()) < 65 or ord(bomb[0].upper()) > 65 + len(user.board)):
            print(f'Invalid input. The first character must be a letter ranging from A to F.')
            return False

        if (bomb[1].isnumeric() == False):
            print(f'Invalid input. The second character must be a number between 1 and {len(user.board)}.')
            return False

        if (int(bomb[1]) < 1 or int(bomb[1]) > len(user.board)):
            print(f'Invalid input. The second character must be a number between 1 and {len(user.board)}.')
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
        print("For the next prompt, type 'play' to play again,")
        print("'exit' to end the program or 'main' to go back to the main menu.")
        print("")
        while True:
            play_again = input("What would you like to do now? ")
            if (play_again == "play"):
                print("")
                print("New Game!")
                print("")
                del user
                del comp
                Game.run_game()
            elif (play_again == "exit"):
                print("")
                print("I hope you had fun playing!")
                print("Now closing program...")
                sys.exit()
            elif (play_again == "main"):
                Game.main_menu()
            else:
                print("Invalid input, please try again.")
                print("")
        return
    


class Player:
    leviathan_len = 7
    kraken_len = 6
    titan_len = 5
    ravana_len = 4
    zurvan_len = 3
    sephirot_len = 2

    def __init__(self, name, size):
        self.name = name
        self.board_size = size
        self.board = self.set_board_size(size) 
        self.deployments = self.set_board_size(size)
        self.leviathan_num = self.set_number_of_leviathan()
        self.kraken_num = self.set_number_of_kraken()
        self.titan_num = self.set_number_of_titan()
        self.ravana_num = self.set_number_of_ravana()
        self.zurvan_num = self.set_number_of_zurvan()
        self.sephirot_num = self.set_number_of_sephirot()
    
    def set_board_size(self, size):
        return [[' ' for _ in range(size)] for _ in range(size)]
    
    def set_number_of_leviathan(self):
        return 1 if self.board_size > 7 else 0

    def set_number_of_kraken(self):
        return 1 if self.board_size > 6 else 0
    
    def set_number_of_titan(self):
        return 1 if self.board_size > 5 else 0
    
    def set_number_of_ravana(self):
        return 2 if self.board_size > 8 else 1 if self.board_size > 4 else 0

    def set_number_of_zurvan(self):
        return 2 if self.board_size > 8 else 1
    
    def set_number_of_sephirot(self):
        return 3 if self.board_size > 8 else 2
    
    def random_battleship_placement(self):
        battleship_locations = []
        if self.board_size > 7:
            print("Placing Leviathan")
            battleship_locations = self.place_random_battleship(battleship_locations, self.leviathan_len)
            print(f"Current {battleship_locations}")
        if self.board_size > 6:
            print("Placing Kraken")
            battleship_locations = self.place_random_battleship(battleship_locations, self.kraken_len)
            print(f"Current {battleship_locations}")
        if self.board_size > 5:
            print("Placing Titan")
            battleship_locations = self.place_random_battleship(battleship_locations, self.titan_len)
            print(f"Current {battleship_locations}")
        if self.board_size > 4:
            print("Placing Ravana")
            battleship_locations = self.place_random_battleship(battleship_locations, self.ravana_len)
            print(f"Current {battleship_locations}")
        if self.board_size == 9:
            print("Placing Ravana")
            battleship_locations = self.place_random_battleship(battleship_locations, self.ravana_len)
            print(f"Current {battleship_locations}")
        if self.board_size > 3:
            print("Placing Zurvan")
            battleship_locations = self.place_random_battleship(battleship_locations, self.zurvan_len)
            print(f"Current {battleship_locations}")
        if self.board_size == 9:
            print("Placing Zurvan")
            battleship_locations = self.place_random_battleship(battleship_locations, self.zurvan_len)
            print(f"Current {battleship_locations}")
        if self.board_size > 3:
            print("Placing Sephirot")
            battleship_locations = self.place_random_battleship(battleship_locations, self.sephirot_len)
            print(f"Current {battleship_locations}")
        if self.board_size > 3:
            print("Placing Sephirot")
            battleship_locations = self.place_random_battleship(battleship_locations, self.sephirot_len)
            print(f"Current {battleship_locations}")
        if self.board_size == 9:
            print("Placing Sephirot")
            battleship_locations = self.place_random_battleship(battleship_locations, self.sephirot_len)
            print(f"Current {battleship_locations}")
        return battleship_locations

    def place_random_battleship(self, battleship_locations, ship_len):
        while True:
            i = random.randint(0, self.board_size - 1)
            j = random.randint(0, self.board_size - 1)
            if (i > self.board_size - ship_len and j > self.board_size - ship_len):
                continue
            location_already_exists = False
            vertical = random.randint(0, 1)
            new_ship = []
            for count in range(ship_len):
                if i > self.board_size - ship_len:
                    new_location = [i, j + count]
                elif j > self.board_size - ship_len:
                    new_location = [i + count, j]
                else:
                    new_location = [i, j + count] if vertical == 1 else [i + count, j]
                if new_location in battleship_locations:
                    location_already_exists = True
                    break
                new_ship.append(new_location)
            if location_already_exists == False:
                for coordinate in new_ship:
                    battleship_locations.append(coordinate)
                self.add_locations_to_game_board(new_ship, ship_len)
                return battleship_locations
            else:
                continue
    
    def add_locations_to_game_board(self, battleship_locations, ship_len):
        for j, sub_array in enumerate(self.board):
            for i, element in enumerate(sub_array):
                if ([i, j] in battleship_locations):
                    self.board[j][i] = Player.print_battleship_character(ship_len)
    
    def print_battleship_character(ship_len):
        if ship_len == 7:
            return "L"
        elif ship_len == 6:
            return "K"
        elif ship_len == 5:
            return "T"
        elif ship_len == 4:
            return "R"
        elif ship_len == 3:
            return "Z"
        else:
            return "S"
    
    def calculate_available_battleship_positions(self, ship_len):
        # In this method, I want to be able to calculate all available positions for any battleship.
        # Define an empty list
        available_positions = []
        # Iterate through user.board
        for j, sub_array in enumerate(self.board):
            for i, element in enumerate(sub_array):
                # If a cell is empty...
                if element == " ":
                    # Run a check to see if ship of a certain length can be placed there.
                    # Run the check both horizontally and vertically in both directions.
                    if (i + ship_len <= self.board_size or i - ship_len >= -1 or j + ship_len <= self.board_size or j - ship_len >= -1):
                        available_positions.append(Player.convert_coordinate_to_cell_name(i, j))
        return available_positions
    
    def convert_coordinate_to_cell_name(i, j):
        return f"{chr(i + 65)}{j + 1}"

    def manual_battleship_placement(self, ):
        return

    def generate_game_board(self):
        # Section to come up with locations
        locations = []
        while (len(locations) < len(self.board)):
            i = random.randint(0, len(self.board) - 1)
            j = random.randint(0, len(self.board) - 1)
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
        print(f"  {self.print_column_headers()}           {self.print_column_headers()}")
        for i, row in enumerate(self.board):
            print(f"{str(i + 1)} {' '.join(row)}          {str(i + 1)} {' '.join(self.deployments[i])}")
        print("")
    
    def print_column_headers(self):
        string = ""
        for i in range(len(self.board)):
            string += chr(65 + i)
            string += " "
        return string

    def update_game_board(self, other, i, j):
        if other.board[j][i] in ["X", "O"]:
            print(f"{self.name} has already deployed a bomb at this location")
            print("")
            return
        elif (other.board[j][i] == " "):
            print(f"{self.name} missed.")
            other.board[j][i] = "X"
        elif (other.board[j][i] in ["L", "K", "T", "R", "Z", "S"]):
            print("It's a hit!")
            other.board[j][i] = "O"
        print("")
        self.deployments[j][i] = other.board[j][i]
        return
    
    def random_move(self):
        while True:
            i = random.randint(0, len(self.board) - 1)
            j = random.randint(0, len(self.board) - 1)
            if self.deployments[j][i] in ["X", "O"]:
                continue
            else:
                computer_move = [i, j]
                return computer_move
    
    def check_win_condition(self, other):
        if any(char in ['L', 'K', 'T', 'R', 'Z', 'S'] for sublist in other.board for char in sublist):
            return False
        else:
            self.print_board()
            other.print_board()
            print(f'Game Over! {self.name} wins!!')
            print("")
            return True

Game.welcome_to_the_game()