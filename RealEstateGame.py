# Author: Stella Wong
# GitHub username: wonste
# Date: 06/03/22
# Description: The program is a very simplified version of Monopoly. The program will only allow for players to roll a
# single die (from 1 - 6) and moving across the board in a circular motion. There is no Jail but there are properties to
# be bought and money to be received for passing GO each time.

class Player:
    """

    """
    def __init__(self, player_name, account_balance, player_position):
        self._player_name = player_name
        self._account_balance = account_balance
        self._player_position = player_position

    def get_player_name(self):
        return self._player_name

    def get_player_position(self):
        return self._player_position

    def get_player_account_balance(self):
        return self._account_balance


class RealEstateGame:
    """
    Represents the game
    """

    def __init__(self):
        self._board_spaces = {}
        self._players = {}

    def create_spaces(self, money, rent_array):
        """
        Creates a total 25 board spaces for the Real Estate Game
        """
        # initiate counter for rent_array
        value = 0

        # iterate through the total amount of board spaces
        for index in range(0, 25):
            # establish go
            if index == 0:
                # [name, rent, purchase, owner]
                go_space = [index, money, None, None]
                self._board_spaces[index] = go_space

            if index > 0:
                # [name, rent, purchase, owner] -> 0, 1, 2, 3
                property_list = [index, rent_array[value], rent_array[value] * 5, None]
                self._board_spaces[index] = property_list
                value += 1

    def create_player(self, user_name, account_balance):
        """
        Create player profiles with given names and starts the players at GO.
        """
        position = 0

        self._players[user_name] = Player(user_name, account_balance, position)

    def get_player_account_balance(self, user_name):
        """
        Obtains specified player name to return the player's account balance.
        """
        for name in self._players:

            if user_name == name:
                person = self._players[user_name]
                total_funds = person.get_player_account_balance()
                return total_funds

    def get_player_current_position(self, user_name):
        """
        Function returns specified player's current position on the board.
        """
        for name in self._players:
            if user_name == name:
                person = self._players[user_name]
                current_position = person.get_player_position()
                return current_position

    def buy_space(self, user_name):
        """
        Checks whether current board space has been purchased by another player, if not, current player can purchase
        current board property if they have enough funds. If already owned by someone else, current player will not be
        allowed to purchase the property.
        """
        person = self._players[user_name]
        player_balance = person.get_player_account_balance()
        player_position = person.get_player_position()
        game_board = self._board_spaces

        # validate that player position is within game board range
        if player_position in game_board:
            # validate that player is not at GO
            if player_position != 0:

                # match board space to player position
                for spot in game_board:

                    if player_position == spot:
                        space_purchase = self._board_spaces[spot][2]

                        # validate player balance >= purchase price
                        if player_balance >= space_purchase:

                            # validate that the board space is purchasable
                            if self._board_spaces[spot][3] is None:
                                player_balance -= space_purchase
                                self._board_spaces[spot][3] = user_name
                                return True
                            else:
                                return False
            else:
                return False

    def move_player(self, user_name, travel_amount):
        """

        """
        person = self._players[user_name]
        player_balance = person.get_player_account_balance()
        player_position = person.get_player_position()

        for individual in self._players:

            if user_name == individual:

                if player_balance == 0:
                    # If the player's account balance is 0, the method will return immediately without doing anything
                    return

                # dice roll ranges from 1 to 6
                if 6 >= travel_amount >= 1:
                    player_position += travel_amount

                    if player_position > 24:
                        player_balance += self._board_spaces[0][1]
                        if player_position == 25:
                            # reset player position so player is at GO
                            player_position = 0
                        if player_position > 25:
                            # reduce to be within board space range
                            player_position -= 25

                            for board_number in self._board_spaces:

                                if player_position == board_number:





    # def check_game_over(self):

        # game is over if all players but one have an account of 0

        # if game is over, the method returns the winning player's name
        # otherwise, method returns winner's name
        # else: method returns an empty string

