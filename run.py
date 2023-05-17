# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import sys
import time
import pdb

class Game:
    """
    A class to represent the game - Battleships Bonanza.
    
    ...

    Methods
    -------
    welcome_to_the_game():
        Prints a welcome message to the user.
    main_menu():
        Asks the user what they would like to do.
    run_game():
        Runs the game.
    ask_user_for_board_size():
        Asks the user what board size they wish to play.
    ask_user_for_random_or_manual_placement_of_battlships():
        Asks the user whether they would like to place ships themselves or get a random assignment of battleships.
    random_placement():
        Randomly assigns battleship places for user.
    manual_placement():
        Allows user to assign their own positions for battleships.
    set_computer_game_board():
        Randomly assigns battleship places for the computer.
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
        print(" Welcome to Battleships Bonanza!")
        print("")
        print(" Developed by Patrick Vieira")
        print("")
        print(" This game of battleships is a two player game. You will be facing off against")
        print(" the computer. Both you and the computer will take turns guessing where each")
        print(" other's battleships are located. The first player to find all of their")
        print(" opponent's battleships is the winner.")
        print("")
        print(" During play, you will only be able to see your own game board. Once the game")
        print(" has finished, the computer's game board will be revealed.")
        print("")
        print(" You will have the option of picking from different board sizes. You will also")
        print(" have the option to place battleships on your board yourself, or you can choose")
        print(" to generate a random board for a quicker start.")
        print("")
        print(" Please follow the instructions given at each stage, and I hope you enjoy the")
        print(" game!")
        Game.main_menu()
    
    def main_menu():
        print("")
        print("")
        print(" Main Menu")
        print("")
        while True:
            command = input(" Type 'play' to play the game or 'exit' to exit: ")
            if command == "play":
                Game.run_game()
            elif command == "exit":
                sys.exit()
            else:
                print(" Invalid command. Please try again.")
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
        print("")
        print("")
        print(" Board Size Selection")
        print("")
        print(" You can now set the size of the board you wish to play. For example:")
        print(" Entering '4' will set the board to a 4 by 4 grid...")
        print(" and entering '8' will set the board to an 8 by 8 grid.")
        print(" You can choose from any number between 4 and 9 inclusive.")
        print(" Please consider that the size you select will determine the duration")
        print(" of the game.")
        while True:
            print("")
            try:
                size = int(input(" What size of board would you like? "))
                if size not in range(4, 10):
                    raise ValueError(" Invalid input. Please enter a number between 4 and 9 inclusive.")
                return size
            except:
                print(" Invalid input. Please enter a number between 4 and 9 inclusive.")
    
    def ask_user_for_random_or_manual_placement_of_battlships(user, comp):
        print("")
        print("")
        print("")
        print(" Battleship Placement Method")
        print("")
        print(" You now have the option to place battleships on the board yourself, or ask")
        print(" the program to set a random one for you. Don't worry! Even if the computer")
        print(" makes it up for you, your opponent doesn't know where your battleships are! :)")
        while True:
            print("")
            string = input(" Type 'r' for random battleship placement or type 'm' to place them yourself: ")
            if string == 'r':
                Game.random_placement(user, comp)
            elif string == 'm':
                Game.manual_placement_welcome(user, comp)
            else:
                print(" Invalid input, please try again.")
    
    def random_placement(user, comp):
        battleship_locations = user.random_battleship_placement()
        print("")
        print("")
        print("")
        print(" Thank you for your selection. Generating random game board...")
        print(" Done!")
        print("")
        Game.set_computer_game_board(user, comp)

    def manual_placement_welcome(user, comp):
        print("")
        print("")
        print("")
        print(" Placing battleships manually.")
        print("")
        print(" You will now be asked to enter the name of the cell where you would like one")
        print(" end of the battleship to start at. Then, depending on the possible")
        print(" orientations from that position, you will be asked to enter further")
        print(" information. For example: if the battleship could be placed horizontally or")
        print(" vertically, you must specify this. If the battleship could be placed")
        print(" horizontally, facing left or right, you must also specify this.")
        print(" The game will ask you to specify if needed.")
        Game.manual_placement(user, comp)
    
    def manual_placement(user, comp):
        battleship_instances = Battleship.get_all_instances()
        for battleship in battleship_instances:
            # Check if battleship can be placed on board
            if not user.battleship_can_be_placed_on_board(battleship.len, battleship.version):
                continue
            print("")
            user.print_board()
            print("")
            # Variable 'positions' is a list of cell names, e.g. ["A1", "B1", ...] etc.
            positions = user.calculate_available_battleship_positions(battleship.len)
            # When printing my variable 'positions', I could use a function to return a string - better readability.
            print(f" The {battleship.name} is a battleship that takes up {battleship.len} cells.")
            print(f" The {battleship.name}'s position can start from the following cells:")
            Player.print_available_positions(positions)
            while True:
                print("")
                user_input = input(f" Type the name of the cell you would like your {battleship.name} to start at: ")
                # If input is not in available cells: continue
                if user_input not in positions:
                    print(" Invalid input, please try again.")
                    continue
                break
            print("")
            # Check if battleship can be placed horizontal and / or vertical
            i, j = Player.convert_cell_name_to_coordinate(user_input)
            # pdb.set_trace()
            if user.battleship_can_be_placed_horizontally(i, j, battleship.len) and user.battleship_can_be_placed_vertically(i, j, battleship.len):
                print(f" This {battleship.name} can be placed horizontally or vertically from {user_input}.")
                print(" Would you like to place it horizontally or vertically?")
                while True:
                    print("")
                    orientation = input(" Type 'h' for horizontal or 'v' for vertical: ")
                    print("")
                    if orientation not in ['h', 'v']:
                        print(" Invalid input. Please try again.")
                        continue
                    break
                if orientation == 'h':
                    # Place it horizontally
                    print(" Placing Horizontally")
                    if user.battleship_can_be_placed_facing_right(i, j, battleship.len) and user.battleship_can_be_placed_facing_left(i, j, battleship.len):
                        print(f" This {battleship.name} can be placed facing left or right from {user_input}.")
                        while True:
                            print("")
                            direction = input(f" Type 'l' to face the {battleship.name} left or 'r' to face it right.")
                            if direction not in ['l', 'r']:
                                print(" Invalid input. Please try again.")
                                continue
                            user.manual_battleship_placement(user_input, direction, battleship.char, battleship.len)
                            break
                    elif user.battleship_can_be_placed_facing_right(i, j, battleship.len):
                        direction = 'r'
                        print(f" This {battleship.name} will now be placed facing right from {user_input}.")
                        user.manual_battleship_placement(user_input, direction, battleship.char, battleship.len)
                    else:
                        direction = 'l'
                        print(f" This {battleship.name} will now be placed facing left from {user_input}.")
                        user.manual_battleship_placement(user_input, direction, battleship.char, battleship.len)
                elif orientation == 'v':
                    # Place it vertically
                    print(" Placing Vertically")
                    if user.battleship_can_be_placed_facing_down(i, j, battleship.len) and user.battleship_can_be_placed_facing_up(i, j, battleship.len):
                        print(f" This {battleship.name} can be placed facing down or up from {user_input}.")
                        while True:
                            print("")
                            direction = input(f" Type 'd' to face the {battleship.name}down or 'u' to face it up.")
                            if direction not in ['d', 'u']:
                                print(" Invalid input. Please try again.")
                                continue
                            user.manual_battleship_placement(user_input, direction, battleship.char, battleship.len)
                            break
                    elif user.battleship_can_be_placed_facing_down(i, j, battleship.len):
                        direction = 'd'
                        print(f" This {battleship.name} will now be placed facing down from {user_input}.")
                        user.manual_battleship_placement(user_input, direction, battleship.char, battleship.len)
                    else:
                        direction = 'u'
                        print(f" This {battleship.name} will now be placed facing up from {user_input}.")
                        user.manual_battleship_placement(user_input, direction, battleship.char, battleship.len)
            elif user.battleship_can_be_placed_horizontally(i, j, battleship.len):
                # Check if battleship can be placed facing right and left
                if user.battleship_can_be_placed_facing_right(i, j, battleship.len) and user.battleship_can_be_placed_facing_left(i, j, battleship.len):
                    print(f" This {battleship.name} can be placed facing left or right from {user_input}.")
                    while True:
                        print("")
                        direction = input(f" Type 'l' to face the {battleship.name} left or 'r' to face it right.")
                        if direction not in ['l', 'r']:
                            continue
                        user.manual_battleship_placement(user_input, direction, battleship.char, battleship.len)
                        break
                elif user.battleship_can_be_placed_facing_right(i, j, battleship.len):
                    direction = 'r'
                    print(f" This {battleship.name} will now be placed facing right from {user_input}.")
                    user.manual_battleship_placement(user_input, direction, battleship.char, battleship.len)
                else:
                    direction = 'l'
                    print(f" This {battleship.name} will now be placed facing left from {user_input}.")
                    user.manual_battleship_placement(user_input, direction, battleship.char, battleship.len)
                print("")
            else:
                # Battleship must be able to be placed vertically.
                # Check if battleship can be placed facing up or down
                print(" Placing Vertically")
                if user.battleship_can_be_placed_facing_down(i, j, battleship.len) and user.battleship_can_be_placed_facing_up(i, j, battleship.len):
                    print(f" This {battleship.name} can be placed facing down or up from {user_input}.")
                    while True:
                        print("")
                        direction = input(f" Type 'd' to face the {battleship.name}down or 'u' to face it up.")
                        if direction not in ['d', 'u']:
                            print(" Invalid input. Please try again.")
                            continue
                        user.manual_battleship_placement(user_input, direction, battleship.char, battleship.len)
                        break
                elif user.battleship_can_be_placed_facing_down(i, j, battleship.len):
                    direction = 'd'
                    print(f" This {battleship.name} will now be placed facing down from {user_input}.")
                    user.manual_battleship_placement(user_input, direction, battleship.char, battleship.len)
                else:
                    direction = 'u'
                    print(f" This {battleship.name} will now be placed facing up from {user_input}.")
                    user.manual_battleship_placement(user_input, direction, battleship.char, battleship.len)
        Game.set_computer_game_board(user, comp)
    
    def set_computer_game_board(user, comp):
        print(" Setting up Computer Board....")
        battleship_locations = comp.random_battleship_placement()
        print(" Done!")
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
            bomb_location = input(" Type where you would like to place your bomb (e.g. A1): ")
            stripped_bomb = bomb_location.replace(" ", "")
            if (Game.validate_bomb_deployment(stripped_bomb, user)):
                # Go to handle_bomb_deployment.
                return stripped_bomb
            else:
                print(" Please try again.")
                print("")
    
    def validate_bomb_deployment(bomb, user):
        if (len(bomb) != 2):
            print(f' Invalid input. String must be 2 characters long.')
            return False

        if (bomb[0].isalpha() == False):
            print(f' Invalid input. The first character must be a letter ranging from A to F.')
            return False

        if (ord(bomb[0].upper()) < 65 or ord(bomb[0].upper()) > 65 + len(user.board)):
            print(f' Invalid input. The first character must be a letter ranging from A to F.')
            return False

        if (bomb[1].isnumeric() == False):
            print(f' Invalid input. The second character must be a number between 1 and {len(user.board)}.')
            return False

        if (int(bomb[1]) < 1 or int(bomb[1]) > len(user.board)):
            print(f' Invalid input. The second character must be a number between 1 and {len(user.board)}.')
            return False

        # I could also check to see if the user has already deployed a bomb at that location but that's a skill issue imo.
        
        else:
            return True

    def handle_bomb_deployment(user, comp, bomb):
        # Logic to update comp game board.
        print("")
        print(f" Approved. The bomb will now be deployed at {bomb[0].upper()}{bomb[1]}.")
        i = ord(bomb[0].upper()) - 65
        j = int(bomb[1]) - 1
        user.update_game_board(comp, i, j)
        return

    def comp_makes_a_move(user, comp):
        # Computer to do a move.
        computer_move = comp.random_move()
        print(f" Computer deploying at {chr(computer_move[0]+65)}{computer_move[1] + 1}.")
        comp.update_game_board(user, computer_move[0], computer_move[1])
        return
    
    def ask_if_user_wishes_to_play_again(user, comp):
        # Ask user if they wish to play the game again.
        print(" For the next prompt, type 'play' to play again, 'exit' to")
        print(" end the program or 'main' to go back to the main menu.")
        print("")
        while True:
            play_again = input(" What would you like to do now? ")
            if (play_again == "play"):
                print("")
                print(" New Game!")
                print("")
                del user
                del comp
                Game.run_game()
            elif (play_again == "exit"):
                print("")
                print(" I hope you had fun playing!")
                print(" Now closing program...")
                sys.exit()
            elif (play_again == "main"):
                Game.main_menu()
            else:
                print(" Invalid input, please try again.")
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
            battleship_locations = self.place_random_battleship(battleship_locations, self.leviathan_len)
        if self.board_size > 6:
            battleship_locations = self.place_random_battleship(battleship_locations, self.kraken_len)
        if self.board_size > 5:
            battleship_locations = self.place_random_battleship(battleship_locations, self.titan_len)
        if self.board_size > 4:
            battleship_locations = self.place_random_battleship(battleship_locations, self.ravana_len)
        if self.board_size == 9:
            battleship_locations = self.place_random_battleship(battleship_locations, self.ravana_len)
        if self.board_size > 3:
            battleship_locations = self.place_random_battleship(battleship_locations, self.zurvan_len)
        if self.board_size == 9:
            battleship_locations = self.place_random_battleship(battleship_locations, self.zurvan_len)
        if self.board_size > 3:
            battleship_locations = self.place_random_battleship(battleship_locations, self.sephirot_len)
        if self.board_size > 3:
            battleship_locations = self.place_random_battleship(battleship_locations, self.sephirot_len)
        if self.board_size == 9:
            battleship_locations = self.place_random_battleship(battleship_locations, self.sephirot_len)
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
                    # Run the check both horizontally and vertically, and in both directions.
                    # Run a further check to see if another ship is blocking our path
                    if not self.other_battleships_to_the_right(i, j, ship_len):
                        available_positions.append(Player.convert_coordinate_to_cell_name(i, j))
                    elif not self.other_battleships_to_the_left(i, j, ship_len):
                        available_positions.append(Player.convert_coordinate_to_cell_name(i, j))
                    elif not self.other_battleships_downwards(i, j, ship_len):
                        available_positions.append(Player.convert_coordinate_to_cell_name(i, j))
                    elif not self.other_battleships_upwards(i, j, ship_len):
                        available_positions.append(Player.convert_coordinate_to_cell_name(i, j))
        return available_positions
    
    def other_battleships_to_the_right(self, i, j, ship_len):
        if i + ship_len <= self.board_size:
            for col in range(i, i + ship_len):
                if not self.board[j][col] == " ":
                    return True
        else:
            return True
        

    def other_battleships_to_the_left(self, i, j, ship_len):
        if i - ship_len >= -1:
            for col in range(i - ship_len + 1, i + 1):
                if not self.board[j][col] == " ":
                    return True
        else:
            return True

    def other_battleships_downwards(self, i, j, ship_len):
        if j + ship_len <= self.board_size:
            for row in range(j, j + ship_len):
                if not self.board[row][i] == " ":
                    return True
        else:
            return True
    
    def other_battleships_upwards(self, i, j, ship_len):
        if j - ship_len >= -1:
            for row in range(j - ship_len + 1, j + 1):
                if not self.board[row][i] == " ":
                    return True
        else:
            return True

    def battleship_can_be_placed_horizontally(self, i, j, ship_len):
        return not (self.other_battleships_to_the_right(i, j, ship_len) and self.other_battleships_to_the_left(i, j, ship_len))
    
    def battleship_can_be_placed_vertically(self, i, j, ship_len):
        return not (self.other_battleships_downwards(i, j, ship_len) and self.other_battleships_upwards(i, j, ship_len))
    
    def battleship_can_be_placed_facing_right(self, i, j, ship_len):
        return not (self.other_battleships_to_the_right(i, j, ship_len))

    def battleship_can_be_placed_facing_left(self, i, j, ship_len):
        return not (self.other_battleships_to_the_left(i, j, ship_len))

    def battleship_can_be_placed_facing_down(self, i, j, ship_len):
        return not (self.other_battleships_downwards(i, j, ship_len))

    def battleship_can_be_placed_facing_up(self, i, j, ship_len):
        return not (self.other_battleships_upwards(i, j, ship_len))

    def convert_coordinate_to_cell_name(i, j):
        return f"{chr(i + 65)}{j + 1}"

    def convert_cell_name_to_coordinate(cell):
        return ord(cell[0]) - 65, int(cell[1]) - 1

    def battleship_can_be_placed_on_board(self, length, version):
        return length == 7 and self.board_size > 7 \
        or length == 6 and self.board_size > 6 \
        or length == 5 and self.board_size > 5 \
        or length == 4 and self.board_size > 4 and version == 1 \
        or length == 4 and self.board_size == 9 and version == 2 \
        or length == 3 and self.board_size > 3 and version == 1 \
        or length == 3 and self.board_size == 9 and version == 2 \
        or length == 2 and self.board_size > 3 and (version == 1 or version == 2) \
        or length == 2 and self.board_size == 9 and version == 3

    def manual_battleship_placement(self, cell, direction, char, length):
        i, j = Player.convert_cell_name_to_coordinate(cell)
        for count in range(length):
            if direction == 'r':
                self.board[j][i + count] = char
            elif direction == 'l':
                self.board[j][i - count] = char
            elif direction == 'd':
                self.board[j + count][i] = char
            elif direction == 'u':
                self.board[j - count][i] = char
        return
    
    def print_available_positions(locations):
        terminal_width = 80
        print(" ", end="")
        line_width = 1

        for cell in locations:
            print(cell, end="")
            current_width = line_width + len(cell) + 2
            if current_width >= terminal_width:
                print("")
                print(" ", end="")
                line_width = 1
                continue
            print(", ", end="")
            line_width += len(cell) + 2
        print("")

    def print_board(self):
        print("")
        print("")
        print(f" {self.name}'s board:      {self.name}'s deployments:")
        print("")
        print(f"   {self.print_column_headers()}           {self.print_column_headers()}")
        for i, row in enumerate(self.board):
            print(f" {str(i + 1)} {' '.join(row)}          {str(i + 1)} {' '.join(self.deployments[i])}")
        print("")
    
    def print_column_headers(self):
        string = ""
        for i in range(len(self.board)):
            string += chr(65 + i)
            string += " "
        return string

    def update_game_board(self, other, i, j):
        if other.board[j][i] in ["X", "O"]:
            print(f" {self.name} has already deployed a bomb at this location")
            print("")
            return
        elif (other.board[j][i] == " "):
            print(f" {self.name} missed.")
            other.board[j][i] = "X"
        elif (other.board[j][i] in ["L", "K", "T", "R", "Z", "S"]):
            print(" It's a hit!")
            other.board[j][i] = "O"
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
            print(f' Game Over! {self.name} wins!!')
            print("")
            return True

class Battleship:
    all_instances = []

    def __init__(self, name, length, char, version):
        self.name = name
        self.len = length
        self.char = char
        self.version = version
        Battleship.all_instances.append(self)
    
    def get_all_instances():
        return Battleship.all_instances
    
leviathan = Battleship("Leviathan", 7, "L", 1)
kraken = Battleship("Kraken", 6, "K", 1)
titan = Battleship("Titan", 5, "T", 1)
ravana1 = Battleship("Ravana", 4, "R", 1)
ravana2 = Battleship("Ravana", 4, "R", 2)
zurvan1 = Battleship("Zurvan", 3, "Z", 1)
zurvan2 = Battleship("Zurvan", 3, "Z", 2)
sephirot1 = Battleship("Sephirot", 2, "S", 1)
sephirot2 = Battleship("Sephirot", 2, "S", 2)
sephirot3 = Battleship("Sephirot", 2, "S", 3)

Game.welcome_to_the_game()