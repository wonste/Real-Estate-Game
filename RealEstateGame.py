# Author: Stella Wong
# GitHub username: wonste
# Date: 06/03/22
# Description: The program is a very simplified version of Monopoly. The program will only allow for players to roll a
# single die (from 1 - 6) and moving across the board in a circular motion. There is no Jail but there are properties to
# be bought and money to be received for passing GO each time.

class Player:

    def __init__(self, player_name, account_balance, player_position):
        self._player_name = player_name
        self._account_balance = account_balance
        self._player_position = player_position

    def get_player_account_balance(self):
        return self._account_balance

    def get_player_name(self):
        return self._player_name

    def get_player_position(self):
        return self._player_position


class RealEstateGame:
    """
    Represents the game
    """

    def __init__(self):
        self._board_spaces = {}
        self._players = {}

    def get_player_via_name(self, user_name):
        player = Player(user_name)
        return player

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
                self._board_spaces[index] = money

            if index > 0:
                self._board_spaces[index] = rent_array[value]
                value += 1

    def create_player(self, user_name, account_balance):
        """
        Create player profiles with given names and starts the players at GO.
        """
        position = 0
        #player_info = {'account balance': account_balance,
        #               'position': position}

        #self._players[user_name] = player_info
        player = Player(user_name, account_balance, position)
        self._players[user_name] = player


    def get_player_account_balance(self, user_name):
        """
        Obtains specified player name to return the player's account balance.
        """
        for name in self._players:

            if user_name == name:
                return self._players[user_name]['account balance']

    def get_player_current_position(self, user_name):
        """
        Function returns specified player's current position on the board.
        """
        for name in self._players:
            if user_name == name:
                return self._players[user_name]['position']

    def buy_space(self, player_name):
