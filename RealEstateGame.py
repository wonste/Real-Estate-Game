# Author: Stella Wong
# GitHub username: wonste
# Date: 06/03/22
# Description: The program is a very simplified version of Monopoly. The program will only allow for players to roll a
# single die (from 1 - 6) and moving across the board in a circular motion. There is no Jail but there are properties to
# be bought and money to be received for passing GO each time.

class Player:

    def __init__(self, player_name, account_balance):
        self._player_name = player_name

        self._owned_properties = []

    def get_player_name(self):
        return self._player_name


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
                self._board_spaces[index] = money

            if index > 0:
                self._board_spaces[index] = rent_array[value]
                value += 1

    def create_player(self, player_name, account_balance):
        """
        Create player profiles
        """
        self._players[player_name] = account_balance

    def get_player_account_balance(self, player_name):

        for name in self._players:
            if player_name == name:
                return self._players[player_name]
