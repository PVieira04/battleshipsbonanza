# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import sys


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
        Asks the user whether they would like to place ships themselves
        or get a random assignment of battleships.
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
        """
        Prints a welcome message to the user and waits for the user to press
        Enter before moving onto the main menu.

                Parameters:
                        None.2

                Returns:
                        Nothing.
        """
        print(" Welcome to Battleships Bonanza!")
        print("")
        print(" Developed by Patrick Vieira")
        print("\n" * 2, end="")
        print(
            " This game of battleships is a one player game. You will be"
            " facing off against"
        )
        print(
            " the computer. Both you and the computer will take turns guessing"
            " where each"
        )
        print(
            " other's battleships are located. The first player to find all of"
            " their"
        )
        print(" opponent's battleships is the winner.")
        print("")
        print(
            " During play, you will only be able to see your own game board."
            " Once the game"
        )
        print(" has finished, the computer's game board will be revealed.")
        print("")
        print(
            " You will have the option of picking from different board sizes."
            " You will also"
        )
        print(
            " have the option to place battleships on your board yourself, or"
            " you can choose"
        )
        print(" to generate a random board for a quicker start.")
        print("\n" * 2, end="")
        print(
            " Please follow the instructions given at each stage, and I hope"
            " you enjoy the"
        )
        print(" game!")
        print("\n" * 2, end="")
        input(" Press the 'Enter' key to continue to the main menu. ")
        Game.main_menu()

    def main_menu():
        """
        Waits for the user to enter a valid command.

                Parameters:
                        None.

                Returns:
                        Nothing.
        """
        print("\n" * 14, end="")
        print(" Main Menu")
        print("")
        while True:
            command = input(
                " Type 'play' to play the game or 'exit' to exit: ")
            if command == "play":
                Game.run_game()
            elif command == "exit":
                sys.exit()
            else:
                print(" Invalid command. Please try again.")
                print("")

    def run_game():
        """
        Creates two instances of the Player class.
        One is the user and the other is the computer.
        This method calls another method.

                Parameters:
                        None.

                Returns:
                        Nothing.
        """
        # Initialise the game.
        size = Game.ask_user_for_board_size()
        user = Player("User", size)
        comp = Player("Computer", size)
        Game.ask_user_for_random_or_manual_placement_of_battlships(user, comp)
        # Game.set_game_boards(user, comp)

    def ask_user_for_board_size():
        """
        Asks for user input and returns it if it is a number between 4 and 9.

                Parameters:
                        None.

                Returns:
                        size (int): number between 4 and 9.
        """
        print("\n" * 9, end="")
        print(" Board Size Selection")
        print("\n" * 2, end="")
        print(
            " You can now set the size of the board you wish to play. For"
            " example:"
        )
        print(" Entering '4' will set the board to a 4 by 4 grid...")
        print(" and entering '8' will set the board to an 8 by 8 grid.")
        print(" You can choose from any number between 4 and 9 inclusive.")
        print(
            " Please consider that the size you select will determine the"
            " duration"
        )
        print(" of the game.")
        while True:
            print("")
            try:
                size = int(input(" Board size: "))
                if size not in range(4, 10):
                    raise ValueError(
                        " Invalid input. Please enter a number between"
                        " 4 and 9 inclusive."
                    )
                return size
            except ValueError:
                print(
                    " Invalid input. Please enter a number between"
                    " 4 and 9 inclusive."
                )

    def ask_user_for_random_or_manual_placement_of_battlships(user, comp):
        """
        Allows user to decide whether to place battleships manually or
        have the program decide randomly for them.

                Parameters:
                        user (obj): instance of the Person Class
                        comp (obj): instance of the Person Class

                Returns:
                        Nothing.
        """
        print("\n" * 14, end="")
        print(" Battleship Placement Method")
        print("\n" * 2, end="")
        print(
            " You now have the option to place battleships on the board"
            " yourself, or ask"
        )
        print(
            " the program to set a random one for you. Don't worry! Even"
            " if the computer"
        )
        print(
            " makes it up for you, your opponent doesn't know where your"
            " battleships are! :)"
        )
        while True:
            print("")
            string = input(" Type 'r' for random or 'm' for manual: ")
            if string == 'r':
                Game.random_placement(user, comp)
            elif string == 'm':
                Game.manual_placement_welcome(user, comp)
            else:
                print(" Invalid input, please try again.")

    def random_placement(user, comp):
        """
        Calls the functions which sets the computer game board,
        and gives a message to the user to inform them of changes.

                Parameters:
                        user (obj): instance of the Person Class
                        comp (obj): instance of the Person Class

                Returns:
                        Nothing.
        """
        user.random_battleship_placement()
        print("\n" * 10, end="")
        print(" Thank you for your selection. Generating random game board...")
        print(" Done!")
        print("")
        Game.set_computer_game_board(user, comp)

    def manual_placement_welcome(user, comp):
        """
        Introduces the user to the Manual Placement mode.

                Parameters:
                        user (obj): instance of the Person Class
                        comp (obj): instance of the Person Class

                Returns:
                        Nothing.
        """
        print("\n" * 8, end="")
        print(" Placing battleships manually.")
        print("")
        print(
            " You will now be asked to enter the name of the cell where you"
            " would like one"
        )
        print(
            " end of the battleship to start at. Then, depending on the"
            " possible"
        )
        print(
            " orientations from that position, you will be asked to enter"
            " further"
        )
        print(" information.")
        print("")
        print(
            " For example: if the battleship could be placed horizontally"
            " or vertically,"
        )
        print(
            " you must specify this. If the battleship could be placed"
            " horizontally,"
        )
        print(" facing left or right, you must also specify this.")
        print("")
        print(" The game will ask you to specify if needed.")
        print("")
        input(" Press the 'Enter' key to continue. ")
        Game.manual_placement(user, comp)

    def manual_placement(user, comp):
        """
        Allows the user to enter the cells they wish to populate with
        battleships.

                Parameters:
                        user (obj): instance of the Person Class
                        comp (obj): instance of the Person Class

                Returns:
                        Nothing.
        """
        battleship_instances = Battleship.get_all_instances()
        for battleship in battleship_instances:
            # Check if battleship can be placed on board
            if not user.battleship_can_be_placed_on_board(
                battleship.len, battleship.version
            ):
                continue
            print("")
            print("\n" * (11 - user.board_size), end="")
            user.print_board()
            print("")
            # Variable 'positions' is a list of cell names,
            # e.g. ["A1", "B1", ...] etc.
            positions = user.calculate_available_battleship_positions(
                battleship.len)
            # When printing my variable 'positions', I could use a function
            # to return a string - better readability.
            print(
                f" Now, it's your turn to strategically position The"
                f" {battleship.name} battleship."
            )
            print(
                f" This is a battleship that takes up {battleship.len} cells."
            )
            print("")
            print(
                f" The {battleship.name}'s position can start from the"
                f" following cells:"
            )
            Player.print_available_positions(positions)
            while True:
                print("")
                user_input = input(
                    f" Type the name of the cell you would like your"
                    f" {battleship.name} to start at: "
                )
                # If input is not in available cells: continue
                if user_input not in positions:
                    print(" Invalid input, please try again.")
                    continue
                break
            print("")
            # Check if battleship can be placed horizontal and / or vertical
            i, j = Player.convert_cell_name_to_coordinate(user_input)
            # pdb.set_trace()
            if user.battleship_can_be_placed_horizontally(i, j, battleship.len) and user.battleship_can_be_placed_vertically(i, j, battleship.len):  # noqa
                print(
                    f" This {battleship.name} can be placed horizontally"
                    f" or vertically from {user_input}."
                )
                print(
                    " Would you like to place it horizontally or vertically?"
                )
                while True:
                    print("")
                    orientation = input(
                        " Type 'h' for horizontal or 'v' for vertical: ")
                    print("")
                    if orientation not in ['h', 'v']:
                        print(" Invalid input. Please try again.")
                        continue
                    break
                if orientation == 'h':
                    # Place it horizontally
                    print(" Placing Horizontally")
                    if user.battleship_can_be_placed_facing_right(i, j, battleship.len) and user.battleship_can_be_placed_facing_left(i, j, battleship.len):  # noqa
                        print(
                            f" This {battleship.name} can be placed facing"
                            f" left or right from {user_input}."
                        )
                        while True:
                            print("")
                            direction = input(
                                f" Type 'l' to face the {battleship.name}"
                                f" left or 'r' to face it right: ")
                            if direction not in ['l', 'r']:
                                print(" Invalid input. Please try again.")
                                continue
                            user.manual_battleship_placement(
                                user_input, direction,
                                battleship.char, battleship.len
                            )
                            break
                    elif user.battleship_can_be_placed_facing_right(i, j, battleship.len):  # noqa
                        direction = 'r'
                        print(
                            f" This {battleship.name} will now be placed"
                            f" facing right from {user_input}."
                        )
                        user.manual_battleship_placement(
                            user_input, direction,
                            battleship.char, battleship.len
                        )
                    else:
                        direction = 'l'
                        print(
                            f" This {battleship.name} will now be placed"
                            f" facing left from {user_input}."
                        )
                        user.manual_battleship_placement(
                            user_input, direction,
                            battleship.char, battleship.len
                        )
                elif orientation == 'v':
                    # Place it vertically
                    print(" Placing Vertically")
                    if user.battleship_can_be_placed_facing_down(i, j, battleship.len) and user.battleship_can_be_placed_facing_up(i, j, battleship.len):  # noqa
                        print(
                            f" This {battleship.name} can be placed facing"
                            f" down or up from {user_input}."
                        )
                        while True:
                            print("")
                            direction = input(
                                " Type 'd' to face it downwards"
                                " or 'u' for upwards: "
                            )
                            if direction not in ['d', 'u']:
                                print(" Invalid input. Please try again.")
                                continue
                            user.manual_battleship_placement(
                                user_input, direction,
                                battleship.char, battleship.len
                            )
                            break
                    elif user.battleship_can_be_placed_facing_down(i, j, battleship.len):  # noqa
                        direction = 'd'
                        print(
                            f" This {battleship.name} will now be placed"
                            f" facing down from {user_input}."
                        )
                        user.manual_battleship_placement(
                            user_input, direction,
                            battleship.char, battleship.len
                        )
                    else:
                        direction = 'u'
                        print(
                            f" This {battleship.name} will now be placed"
                            f" facing up from {user_input}."
                        )
                        user.manual_battleship_placement(
                            user_input, direction,
                            battleship.char, battleship.len
                        )
            elif user.battleship_can_be_placed_horizontally(i, j, battleship.len):  # noqa
                # Check if battleship can be placed facing right and left
                if user.battleship_can_be_placed_facing_right(i, j, battleship.len) and user.battleship_can_be_placed_facing_left(i, j, battleship.len):  # noqa
                    print(
                        f" This {battleship.name} can be placed facing"
                        f" left or right from {user_input}."
                    )
                    while True:
                        print("")
                        direction = input(
                            " Type 'l' to face it left or 'r' to"
                            " face it right: "
                        )
                        if direction not in ['l', 'r']:
                            continue
                        user.manual_battleship_placement(
                            user_input, direction,
                            battleship.char, battleship.len
                        )
                        break
                elif user.battleship_can_be_placed_facing_right(i, j, battleship.len):  # noqa
                    direction = 'r'
                    print(
                        f" This {battleship.name} will now be placed facing"
                        f" right from {user_input}.")
                    user.manual_battleship_placement(
                        user_input, direction,
                        battleship.char, battleship.len
                    )
                else:
                    direction = 'l'
                    print(
                        f" This {battleship.name} will now be placed facing"
                        f" left from {user_input}."
                    )
                    user.manual_battleship_placement(
                        user_input, direction,
                        battleship.char, battleship.len
                    )
                print("")
            else:
                # Battleship must be able to be placed vertically.
                # Check if battleship can be placed facing up or down
                print(" Placing Vertically")
                if user.battleship_can_be_placed_facing_down(i, j, battleship.len) and user.battleship_can_be_placed_facing_up(i, j, battleship.len):  # noqa
                    print(
                        f" This {battleship.name} can be placed facing"
                        f" down or up from {user_input}.")
                    while True:
                        print("")
                        direction = input(
                            " Type 'd' to face it downwards or"
                            " 'u' for upwards: "
                        )
                        if direction not in ['d', 'u']:
                            print(" Invalid input. Please try again.")
                            continue
                        user.manual_battleship_placement(
                            user_input, direction,
                            battleship.char, battleship.len
                        )
                        break
                elif user.battleship_can_be_placed_facing_down(i, j, battleship.len):  # noqa
                    direction = 'd'
                    print(
                        f" This {battleship.name} will now be placed facing"
                        f" down from {user_input}."
                    )
                    user.manual_battleship_placement(
                        user_input, direction,
                        battleship.char, battleship.len
                    )
                else:
                    direction = 'u'
                    print(
                        f" This {battleship.name} will now be placed facing"
                        f" up from {user_input}."
                    )
                    user.manual_battleship_placement(
                        user_input, direction,
                        battleship.char, battleship.len
                    )
        Game.set_computer_game_board(user, comp)

    def set_computer_game_board(user, comp):
        """
        Calls the random battleship placement function from comp and
        prepares the user for the next stage through print statements.

                Parameters:
                        user (obj): instance of the Person Class
                        comp (obj): instance of the Person Class

                Returns:
                        Nothing.
        """
        print(" Setting up Computer Board....")
        comp.random_battleship_placement()
        print(" Done!")
        print("")
        print(" All game boards have been generated.")
        print("")
        print(
            " You and the computer will now take turns in"
            " guessing where each others'"
        )
        print(" battleships are located.")
        print("")
        input(" Press the 'Enter' key to continue. ")
        Game.main_game_loop(user, comp)

    def main_game_loop(user, comp):
        """
        Organises the methods used for the main game loop. Function is exited
        upon triggering the win condition.

                Parameters:
                        user (obj): instance of the Person Class
                        comp (obj): instance of the Person Class

                Returns:
                        Nothing.
        """
        # The main game loop runs here. Only exits with winning condition.
        while True:
            Game.display_game_boards(user)
            bomb = Game.ask_user_to_deploy_bombs(user)
            Game.handle_bomb_deployment(user, comp, bomb)
            if (user.check_win_condition(comp)):
                Game.ask_if_user_wishes_to_play_again(user, comp)
            Game.comp_makes_a_move(user, comp)
            if (comp.check_win_condition(user)):
                Game.ask_if_user_wishes_to_play_again(user, comp)

    def display_game_boards(user):
        """
        Calls the print board function from the user object.

                Parameters:
                        user (obj): instance of the Person Class
                        comp (obj): instance of the Person Class

                Returns:
                        Nothing.
        """
        print("\n" * (11 - user.board_size), end="")
        user.print_board()

    def ask_user_to_deploy_bombs(user):
        """
        Allows user to submit their choice of where to attack.

                Parameters:
                        user (obj): instance of the Person Class
                        comp (obj): instance of the Person Class

                Returns:
                        stripped_bomb (str): user input with whitespace
                            stripped
        """
        while (True):
            bomb_location = input(
                " Type where you would like to place your bomb (e.g. A1): ")
            stripped_bomb = bomb_location.replace(" ", "")
            if (Game.validate_bomb_deployment(stripped_bomb, user)):
                # Go to handle_bomb_deployment.
                return stripped_bomb
            print(" Please try again.")
            print("")

    def validate_bomb_deployment(bomb: str, user):
        """
        Returns True or False depending on user input carried forward
        from previous function.

                Parameters:
                        user (obj): instance of the Person Class
                        comp (obj): instance of the Person Class

                Returns:
                        True
                        False
        """
        if (len(bomb) != 2):
            print(" Invalid input. String must be 2 characters long.")
            return False

        if (bomb[0].isalpha() is False):
            print(
                " Invalid input. The first character must be a letter"
                " ranging from A to F."
            )
            return False

        if (ord(bomb[0].upper()) < 65 or ord(bomb[0].upper()) > 65 + len(user.board)):  # noqa
            print(
                " Invalid input. The first character must be a letter"
                " ranging from A to F."
            )
            return False

        if (bomb[1].isnumeric() is False):
            print(
                f" Invalid input. The second character must be a number"
                f" between 1 and {len(user.board)}."
            )
            return False

        if (int(bomb[1]) < 1 or int(bomb[1]) > len(user.board)):
            print(
                f" Invalid input. The second character must be a number"
                f" between 1 and {len(user.board)}."
            )
            return False

        return True

    def handle_bomb_deployment(user, comp, bomb):
        """
        Calls the update game board function and passes in the
        coordinates of the cell defined in 'bomb'.

                Parameters:
                        user (obj): instance of the Person Class
                        comp (obj): instance of the Person Class
                        bomb (str): stripped version of the user input from
                            previous function

                Returns:
                        Nothing.
        """
        print("")
        print(
            f" Approved. The bomb will now be deployed"
            f" at {bomb[0].upper()}{bomb[1]}."
        )
        i = ord(bomb[0].upper()) - 65
        j = int(bomb[1]) - 1
        user.update_game_board(comp, i, j)

    def comp_makes_a_move(user, comp):
        """
        Calls functions to randomly select a cell to attack.

                Parameters:
                        user (obj): instance of the Person Class
                        comp (obj): instance of the Person Class

                Returns:
                        Nothing.
        """
        computer_move = comp.random_move()
        print("")
        print(
            f" Computer deploying at"
            f" {chr(computer_move[0]+65)}{computer_move[1] + 1}."
        )
        comp.update_game_board(user, computer_move[0], computer_move[1])

    def ask_if_user_wishes_to_play_again(user, comp):
        """
        Allows user to choose what to do once game has ended.

                Parameters:
                        user (obj): instance of the Person Class
                        comp (obj): instance of the Person Class
                        bomb (str): stripped version of the user input from
                            previous function

                Returns:
                        Nothing.
        """
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


class Player:
    """
    A class to represent a player.

    ...

    Attributes
    ----------
    name : str
        name of the player
    board_size : int
        size of the board
    board : List
        the nested list containing battleships and bombs
    deployments : List
        the nested list containing only deployed bombs
    leviathan_num : int
        number of Leviathan battleships needed for this size of board
    kraken_num : int
        number of Kraken battleships needed for this size of board
    titan_num : int
        number of Titan battleships needed for this size of board
    ravana_num : int
        number of Ravana battleships needed for this size of board
    zurvan_num : int
        number of Zurvan battleships needed for this size of board
    sephirot_num : int
        number of Sephirot battleships needed for this size of board

    Methods
    -------
    set_board_size(size):
        Sets up the correct sized board for the player
    set_number_of_leviathan():
        Sets up number of Leviathan battleships based on board size.
    set_number_of_kraken():
        Sets up number of Kraken battleships based on board size.
    set_number_of_titan():
        Sets up number of Titan battleships based on board size.
    set_number_of_ravana():
        Sets up number of Ravana battleships based on board size.
    set_number_of_zurvan():
        Sets up number of Zurvan battleships based on board size.
    set_number_of_sephirot():
        Sets up number of Sephirot battleships based on board size.
    random_battleship_placement():
        Iterates through all battleships and calls functions to add them to the
        game board.
    place_random_battleship(battleship_locations, ship_len):
        Adds coordinates occupied by a bettleship to battleship_locations
        and returns it.
    add_locations_to_game_board(battleship_locations, ship_len):
        Iterates through all game board elements and adds the correct
        battleship characterto represent it.
    print_battleship_character(ship_len):
        Returns the battleship character based on the ship length.
    calculate_available_battleship_positions(self, ship_len):
        Iterates through the game board and returns a list of all cells the
        battleship can start from.
    other_battleships_to_the_right(self, i, j, ship_len):
        Calculates whether there are other battleships to the right of a
        position on the board.
    other_battleships_to_the_left(self, i, j, ship_len):
        Calculates whether there are other battleships to the left of a
        position on the board.
    other_battleships_downwards(self, i, j, ship_len):
        Calculates whether there are other battleships downwards of a position
        on the board.
    other_battleships_upwards=(self, i, j, ship_len):
        Calculates whether there are other battleships upwards of a position
        on the board.
    battleship_can_be_placed_horizontally(self, i, j, ship_len):
        Calculates whether a bettleship can be placed horizontally or not.
    battleship_can_be_placed_vertically(self, i, j, ship_len):
        Calculates whether a bettleship can be placed vertically or not.
    battleship_can_be_placed_facing_right(self, i, j, ship_len):
        Calculates whether a bettleship can be placed facing right from its
        current position.
    battleship_can_be_placed_facing_left(self, i, j, ship_len):
        Calculates whether a bettleship can be placed facing left from its
        current position.
    battleship_can_be_placed_facing_down(self, i, j, ship_len):
        Calculates whether a bettleship can be placed facing down from its
        current position.
    battleship_can_be_placed_facing_up(self, i, j, ship_len):
        Calculates whether a bettleship can be placed facing up from its
        current position.
    convert_coordinate_to_cell_name(i, j):
        Converts the coordinates of a cell to its cell name.
    convert_cell_name_to_coordinate(cell):
        Converts a position's cell name to its coordinates.
    battleship_can_be_placed_on_board(self, length, version):
        Calculates whether the battleship in question should be placed on
        the board of the given size.
    manual_battleship_placement(self, cell, direction, char, length):
        Replaces the elements on the game board with the character for the
        correct battleship.
    print_available_positions(locations):
        Displays the avilable starting positions of the battleship in
        question in a clear and easily visible manner.
    print_board(self):
        Display's a Player's board and deployments to the terminal side by
        side.
    print_column_headers(self):
        Returns a string containing the column headers based on the size of
        the board.
    update_game_board(self, other, i, j):
        Updates the opponent's game board and user's deployments depending
        on given coordinates.
    random_move(self):
        Returns the coordinates of the computer's next attacking location
        that it hasn't previously targeted.
    check_win_condition(self, other):
        Checks to see whether any battleship characters are left on the
        opponent's board.
    """
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
        """
        Sets up the correct sized board for the player

                Parameters:
                        None.

                Return:
                        a nested List with each element containing a space.
        """
        return [[' ' for _ in range(size)] for _ in range(size)]

    def set_number_of_leviathan(self):
        """
        Sets up number of Leviathan battleships based on board size.

                Parameters:
                        None.

                Return:
                        int
        """
        return 1 if self.board_size > 7 else 0

    def set_number_of_kraken(self):
        """
        Sets up number of Kraken battleships based on board size.

                Parameters:
                        None.

                Return:
                        int
        """
        return 1 if self.board_size > 6 else 0

    def set_number_of_titan(self):
        """
        Sets up number of Titan battleships based on board size.

                Parameters:
                        None.

                Return:
                        int
        """
        return 1 if self.board_size > 5 else 0

    def set_number_of_ravana(self):
        """
        Sets up number of Ravana battleships based on board size.

                Parameters:
                        None.

                Return:
                        int
        """
        return 2 if self.board_size > 8 else 1 if self.board_size > 4 else 0

    def set_number_of_zurvan(self):
        """
        Sets up number of Zurvan battleships based on board size.

                Parameters:
                        None.

                Return:
                        int
        """
        return 2 if self.board_size > 8 else 1

    def set_number_of_sephirot(self):
        """
        Sets up number of Sephirot battleships based on board size.

                Parameters:
                        None.

                Return:
                        int
        """
        return 3 if self.board_size > 8 else 2

    def random_battleship_placement(self):
        """
        Iterates through all battleships and calls functions to add each
        of them to the game board.

                Parameters:
                        None.

                Return:
                        Nothing.
        """
        battleship_locations = []
        if self.board_size > 7:
            battleship_locations = self.place_random_battleship(
                battleship_locations, self.leviathan_len)
        if self.board_size > 6:
            battleship_locations = self.place_random_battleship(
                battleship_locations, self.kraken_len)
        if self.board_size > 5:
            battleship_locations = self.place_random_battleship(
                battleship_locations, self.titan_len)
        if self.board_size > 4:
            battleship_locations = self.place_random_battleship(
                battleship_locations, self.ravana_len)
        if self.board_size == 9:
            battleship_locations = self.place_random_battleship(
                battleship_locations, self.ravana_len)
        if self.board_size > 3:
            battleship_locations = self.place_random_battleship(
                battleship_locations, self.zurvan_len)
        if self.board_size == 9:
            battleship_locations = self.place_random_battleship(
                battleship_locations, self.zurvan_len)
        if self.board_size > 3:
            battleship_locations = self.place_random_battleship(
                battleship_locations, self.sephirot_len)
        if self.board_size > 3:
            battleship_locations = self.place_random_battleship(
                battleship_locations, self.sephirot_len)
        if self.board_size == 9:
            battleship_locations = self.place_random_battleship(
                battleship_locations, self.sephirot_len)

    def place_random_battleship(self, battleship_locations, ship_len):
        """
        Adds coordinates occupied by a battleship to battleship_locations
        and returns it.

                Parameters:
                        battleship_locations (List) : list of coordinates
                            occupied by battleships
                        ship_len (int) : length of the ship being added to
                            the board

                Return:
                        battleship_locations (List) : list of coordinates
                            occupied by battleships
        """
        while True:
            i = random.randint(0, self.board_size - 1)
            j = random.randint(0, self.board_size - 1)
            if (i > self.board_size - ship_len and j > self.board_size - ship_len):  # noqa
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
                    new_location = [
                        i, j + count] if vertical == 1 else [i + count, j]
                if new_location in battleship_locations:
                    location_already_exists = True
                    break
                new_ship.append(new_location)
            if location_already_exists is False:
                for coordinate in new_ship:
                    battleship_locations.append(coordinate)
                self.add_locations_to_game_board(new_ship, ship_len)
                return battleship_locations
            continue

    def add_locations_to_game_board(self, battleship_locations, ship_len):
        """
        Iterates through all game board elements and adds the correct
        battleship character to represent it.

                Parameters:
                        battleship_locations (List) : list of coordinates
                            occupied by battleships
                        ship_len (int) : length of the ship being added to
                            the board

                Return:
                        Nothing.
        """
        for j, sub_array in enumerate(self.board):
            for i, element in enumerate(sub_array):
                if ([i, j] in battleship_locations):
                    self.board[j][i] = Player.print_battleship_character(ship_len)  # noqa

    def print_battleship_character(ship_len):
        """
        Returns the battleship character based on the ship length.

                Parameters:
                        ship_len (int) : length of the ship being added to
                            the board

                Return:
                        str of length 1.
        """
        if ship_len == 7:
            return "L"
        if ship_len == 6:
            return "K"
        if ship_len == 5:
            return "T"
        if ship_len == 4:
            return "R"
        if ship_len == 3:
            return "Z"
        return "S"

    def calculate_available_battleship_positions(self, ship_len):
        """
        Iterates through the game board and returns a list of
        all cells the battleship can start from.

                Parameters:
                        ship_len (int) : length of the ship being added to
                            the board

                Return:
                        available_positions (List) : a list containing cell
                            names of abilable positions.
        """
        # In this method, I want to be able to calculate all available
        # positions for any battleship.
        # Define an empty list
        available_positions = []
        # Iterate through user.board
        for j, sub_array in enumerate(self.board):
            for i, element in enumerate(sub_array):
                # If a cell is empty...
                if element == " ":
                    # Run a check to see if ship of a certain length can be
                    # placed there. Run the check both horizontally and
                    # vertically, and in both directions. Run a further
                    # check to see if another ship is blocking our path.
                    # If the area is free, add the cell name to the
                    # available_positions list.
                    if not self.other_battleships_to_the_right(
                        i, j, ship_len
                    ):
                        available_positions.append(
                            Player.convert_coordinate_to_cell_name(i, j)
                        )
                    elif not self.other_battleships_to_the_left(
                        i, j, ship_len
                    ):
                        available_positions.append(
                            Player.convert_coordinate_to_cell_name(i, j)
                        )
                    elif not self.other_battleships_downwards(
                        i, j, ship_len
                    ):
                        available_positions.append(
                            Player.convert_coordinate_to_cell_name(i, j)
                        )
                    elif not self.other_battleships_upwards(
                        i, j, ship_len
                    ):
                        available_positions.append(
                            Player.convert_coordinate_to_cell_name(i, j)
                        )
        return available_positions

    def other_battleships_to_the_right(self, i, j, ship_len):
        """
        Calculates whether there are other battleships to the right of a
        position on the board.

                Parameters:
                        i (int) : x coordinate of board
                        j (int) : y coordinate of board
                        ship_len (int) : length of the ship being added to
                            the board

                Return:
                        True or False
        """
        if i + ship_len <= self.board_size:
            for col in range(i, i + ship_len):
                if not self.board[j][col] == " ":
                    return True
        else:
            return True

    def other_battleships_to_the_left(self, i, j, ship_len):
        """
        Calculates whether there are other battleships to the left of a
        position on the board.

                Parameters:
                        i (int) : x coordinate of board
                        j (int) : y coordinate of board
                        ship_len (int) : length of the ship being added to
                            the board

                Return:
                        True or False
        """
        if i - ship_len >= -1:
            for col in range(i - ship_len + 1, i + 1):
                if not self.board[j][col] == " ":
                    return True
        else:
            return True

    def other_battleships_downwards(self, i, j, ship_len):
        """
        Calculates whether there are other battleships downwards of a
        position on the board.

                Parameters:
                        i (int) : x coordinate of board
                        j (int) : y coordinate of board
                        ship_len (int) : length of the ship being added to
                            the board

                Return:
                        True or False
        """
        if j + ship_len <= self.board_size:
            for row in range(j, j + ship_len):
                if not self.board[row][i] == " ":
                    return True
        else:
            return True

    def other_battleships_upwards(self, i, j, ship_len):
        """
        Calculates whether there are other battleships upwards of a
        position on the board.

                Parameters:
                        i (int) : x coordinate of board
                        j (int) : y coordinate of board
                        ship_len (int) : length of the ship being added to
                            the board

                Return:
                        True or False
        """
        if j - ship_len >= -1:
            for row in range(j - ship_len + 1, j + 1):
                if not self.board[row][i] == " ":
                    return True
        else:
            return True

    def battleship_can_be_placed_horizontally(self, i, j, ship_len):
        """
        Calculates whether a bettleship can be placed horizontally or not.

                Parameters:
                        i (int) : x coordinate of board
                        j (int) : y coordinate of board
                        ship_len (int) : length of the ship being added to
                            the board

                Return:
                        True or False
        """
        return not (self.other_battleships_to_the_right(i, j, ship_len) and self.other_battleships_to_the_left(i, j, ship_len))  # noqa

    def battleship_can_be_placed_vertically(self, i, j, ship_len):
        """
        Calculates whether a bettleship can be placed vertically or not.

                Parameters:
                        i (int) : x coordinate of board
                        j (int) : y coordinate of board
                        ship_len (int) : length of the ship being added
                            to the board

                Return:
                        True or False
        """
        return not (self.other_battleships_downwards(i, j, ship_len) and self.other_battleships_upwards(i, j, ship_len))  # noqa

    def battleship_can_be_placed_facing_right(self, i, j, ship_len):
        """
        Calculates whether a bettleship can be placed facing right from its
        current position.

                Parameters:
                        i (int) : x coordinate of board
                        j (int) : y coordinate of board
                        ship_len (int) : length of the ship being added to
                            the board

                Return:
                        True or False
        """
        return not (self.other_battleships_to_the_right(i, j, ship_len))

    def battleship_can_be_placed_facing_left(self, i, j, ship_len):
        """
        Calculates whether a bettleship can be placed facing left from its
        current position.

                Parameters:
                        i (int) : x coordinate of board
                        j (int) : y coordinate of board
                        ship_len (int) : length of the ship being added to
                            the board

                Return:
                        True or False
        """
        return not (self.other_battleships_to_the_left(i, j, ship_len))

    def battleship_can_be_placed_facing_down(self, i, j, ship_len):
        """
        Calculates whether a bettleship can be placed facing down from its
        current position.

                Parameters:
                        i (int) : x coordinate of board
                        j (int) : y coordinate of board
                        ship_len (int) : length of the ship being added to
                            the board

                Return:
                        True or False
        """
        return not (self.other_battleships_downwards(i, j, ship_len))

    def battleship_can_be_placed_facing_up(self, i, j, ship_len):
        """
        Calculates whether a bettleship can be placed facing up from its
        current position.

                Parameters:
                        i (int) : x coordinate of board
                        j (int) : y coordinate of board
                        ship_len (int) : length of the ship being added to
                            the board

                Return:
                        True or False
        """
        return not (self.other_battleships_upwards(i, j, ship_len))

    def convert_coordinate_to_cell_name(i, j):
        """
        Converts the coordinates of a cell to its cell name.

                Parameters:
                        i (int) : x coordinate of board
                        j (int) : y coordinate of board

                Return:
                        True or False
        """
        return f"{chr(i + 65)}{j + 1}"

    def convert_cell_name_to_coordinate(cell):
        """
        Converts a position's cell name to its coordinates.

                Parameters:
                        cell (str) : Cell name of two characters

                Return:
                        True or False
        """
        return ord(cell[0]) - 65, int(cell[1]) - 1

    def battleship_can_be_placed_on_board(self, length, version):
        """
        Calculates whether the battleship in question should be placed on the
        board of the given size.

                Parameters:
                        length (int) : length of the ship being added to the
                            board
                        version (int) : version of the battleship being added
                            to the board

                Return:
                        True or False
        """
        return length == 7 and self.board_size > 7 \
            or length == 6 and self.board_size > 6 \
            or length == 5 and self.board_size > 5 \
            or length == 4 and self.board_size > 4 and version == 1 \
            or length == 4 and self.board_size == 9 and version == 2 \
            or length == 3 and self.board_size > 3 and version == 1 \
            or length == 3 and self.board_size == 9 and version == 2 \
            or length == 2 and self.board_size > 3 and version in (1, 2) \
            or length == 2 and self.board_size == 9 and version == 3

    def manual_battleship_placement(self, cell, direction, char, length):
        """
        Replaces the elements on the game board with the character for the
        correct battleship.

                Parameters:
                        cell (str) : The cell name of the battleship's starting
                            position.
                        direction (str) : The direction the battleship is
                            facing.
                        char (str) : The charater that represents the
                            battleship being added to the board.
                        length (int) : The length of the battleship being added
                            to the board.

                Return:
                        Nothing.
        """
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

    def print_available_positions(locations):
        """
        Displays the avilable starting positions of the battleship in question
        in a clear and easily visible manner.

                Parameters:
                        locations (List) : Contains the avilable starting
                            positions of the battleship in question.

                Return:
                        Nothing.
        """
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
            if cell == locations[len(locations) - 2]:
                print(" and ", end="")
                continue
            if cell == locations[len(locations) - 1]:
                print(".", end="")
                break
            print(", ", end="")
            line_width += len(cell) + 2
        print("")

    def print_board(self):
        """
        Display's a Player's board and deployments to the terminal side
        by side.

                Parameters:
                        None.

                Return:
                        Nothing.
        """
        print("")
        print("")
        print(f" {self.name}'s board:      {self.name}'s deployments:")
        print("")
        print(
            f"   {self.print_column_headers()}           "
            f"{self.print_column_headers()}")
        for i, row in enumerate(self.board):
            print(
                f" {str(i + 1)} {' '.join(row)}          "
                f"{str(i + 1)} {' '.join(self.deployments[i])}")
        print("")

    def print_column_headers(self):
        """
        Returns a string containing the column headers based on the size
        of the board.

                Parameters:
                        None.

                Return:
                        Nothing.
        """
        string = ""
        for i in range(len(self.board)):
            string += chr(65 + i)
            string += " "
        return string

    def update_game_board(self, other, i, j):
        """
        Updates the opponent's game board and user's deployments depending
        on given coordinates.

                Parameters:
                        other (obj) : The object of the opponent.
                        i (int) : The x coordinate of the chosen location
                        j (int) : The y coordinate of the chosen location

                Return:
                        Nothing.
        """
        if other.board[j][i] in ["X", "O"]:
            print(f" {self.name} has already deployed a bomb at this location")
            print("")
            return
        if (other.board[j][i] == " "):
            print(f" {self.name} missed.")
            other.board[j][i] = "X"
        if (other.board[j][i] in ["L", "K", "T", "R", "Z", "S"]):
            print(" It's a hit!")
            other.board[j][i] = "O"
        self.deployments[j][i] = other.board[j][i]
        return

    def random_move(self):
        """
        Returns the coordinates of the computer's next attacking location that
        it hasn't previously targeted.

                Parameters:
                        None.

                Return:
                        computer_move (List) : A list containing the
                            coordinates of the computer's chosen location
                            to attack.
        """
        while True:
            i = random.randint(0, len(self.board) - 1)
            j = random.randint(0, len(self.board) - 1)
            if self.deployments[j][i] in ["X", "O"]:
                continue
            computer_move = [i, j]
            return computer_move

    def check_win_condition(self, other):
        """
        Checks to see whether any battleship characters are left on the
        opponent's board.

                Parameters:
                        other (obj) : The object of the opponent.

                Return:
                        True or False
        """
        if any(char in ['L', 'K', 'T', 'R', 'Z', 'S'] for sublist in other.board for char in sublist):  # noqa
            return False
        self.print_board()
        other.print_board()
        print(f' Game Over! {self.name} wins!!')
        print("")
        return True


class Battleship:
    """
    A class to represent a battleship.

    ...

    Attributes
    ----------
    name : str
        name of the battleship
    length : int
        how many cells the battleship takes up
    char : str
        what character represents the battleship on the board
    version : int
        what instance of the same battleship is it
    compatible_boards : List
        list of integers representing what board sizes that battleship can be
        placed on

    Methods
    -------
    get_all_instances():
        Returns the all_instances class variable containing all instanced
        objects.
    """
    all_instances = []

    def __init__(self, name, length, char, version, compatible_boards):
        """
        Constructs all the necessary attributes for the Battleship object.

        Parameters
        ----------
            name : str
                name of the battleship
            length : int
                how many cells the battleship takes up
            char : str
                what character represents the battleship on the board
            version : int
                what instance of the same battleship is it
            compatible_boards : List
                list of integers representing what board sizes that battleship
                can be placed on
        """
        self.name = name
        self.len = length
        self.char = char
        self.version = version
        self.compatible_boards = compatible_boards
        Battleship.all_instances.append(self)

    def get_all_instances():
        """
        Returns the all_instances class variable containing all instanced
        objects.

        Parameters
        ----------
        None

        Returns
        -------
            all_instances : List
                List containing all instanced battleship objects
        """
        return Battleship.all_instances


leviathan = Battleship("Leviathan", 7, "L", 1, [8, 9])
kraken = Battleship("Kraken", 6, "K", 1, [7, 8, 9])
titan = Battleship("Titan", 5, "T", 1, [6, 7, 8, 9])
ravana1 = Battleship("Ravana", 4, "R", 1, [5, 6, 7, 8, 9])
ravana2 = Battleship("Ravana", 4, "R", 2, [9])
zurvan1 = Battleship("Zurvan", 3, "Z", 1, [4, 5, 6, 7, 8, 9])
zurvan2 = Battleship("Zurvan", 3, "Z", 2, [9])
sephirot1 = Battleship("Sephirot", 2, "S", 1, [4, 5, 6, 7, 8, 9])
sephirot2 = Battleship("Sephirot", 2, "S", 2, [4, 5, 6, 7, 8, 9])
sephirot3 = Battleship("Sephirot", 2, "S", 3, [9])

Game.welcome_to_the_game()
