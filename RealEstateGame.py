# Author: Stella Wong
# GitHub username: wonste
# Date: 06/03/22
# Description: The program is a very simplified version of Monopoly. The program will only allow for players to roll a
# single die (from 1 to 6) and moving across the board in a circular motion. There is no Jail but there are properties
# to be bought and money to be received for passing GO each time.

class RealEstateGame:
    """
    Represents the game which is a simplified version of Monopoly.
    """
    def __init__(self):
        self._board_spaces = {}
        self._players = {}
        self._active_players = []

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
        # compile a list of all players participating
        self._active_players.append(user_name)
        # 0, 1, 2
        player_info = [user_name, account_balance, position]
        self._players[user_name] = player_info

    def get_player_account_balance(self, user_name):
        """
        Obtains specified player name to return the player's account balance.
        """
        for name in self._players:
            if user_name == name:
                total_funds = self._players[user_name][1]
                return total_funds

    def get_player_current_position(self, user_name):
        """
        Function returns specified player's current position on the board.
        """
        for name in self._players:
            if user_name == name:
                current_position = self._players[user_name][2]
                return current_position

    def buy_space(self, user_name):
        """
        Checks whether current board space has been purchased by another player, if not, current player can purchase
        current board property if they have enough funds. If already owned by someone else, current player will not be
        allowed to purchase the property.
        """
        current_player_balance = self.get_player_account_balance(user_name)
        player_position = self._players[user_name][2]
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
                        if current_player_balance >= space_purchase:

                            # validate that the board space is purchasable
                            if self._board_spaces[spot][3] is None:
                                self._players[user_name][1] = current_player_balance - space_purchase
                                self._board_spaces[spot][3] = user_name
                                return True
                            else:
                                return False
            else:
                return False

    def move_player(self, user_name, travel_amount):
        """
        Function takes in the player's name and value they "rolled" the dice to move the player forward on the game
        board. The location they land in determines whether the player will pay, earn, or idle depending on their
        conditions. Due to requirements, this is probably the longest and most convoluted method.
        """
        current_player_balance = self.get_player_account_balance(user_name)
        current_player_position = self.get_player_current_position(user_name)
        go_fund = self._board_spaces[0][1]

        if current_player_balance == 0:
            # If the player's account balance is 0, the method will return immediately without doing anything
            return

        # validate dice roll value and toss out unwanted values
        if travel_amount > 6 or travel_amount < 1:
            return

        # add the roll to the current position for total
        self._players[user_name][2] += travel_amount

        if current_player_position == 25:
            # reset player position so player is at GO and pay player
            self._players[user_name][1] += go_fund
            self._players[user_name][2] = 0

        if current_player_position > 25:
            # reduce to be within board space range and pay the player
            self._players[user_name][1] += go_fund
            self._players[user_name][2] = current_player_position - 25

        board_number = current_player_position
        property_owner = self._board_spaces[self.get_player_current_position(user_name)][3]

        if property_owner == user_name:
            return

        if property_owner is not None:
            space_owner = self._players[property_owner]
            rent = self._board_spaces[board_number][1]
            owner_balance = self.get_player_account_balance(property_owner)

            if current_player_balance > self._board_spaces[board_number][1]:
                # adjust player balance with the new deduction

                self._players[user_name][1] = current_player_balance - rent

                # pay the property owner rent
                # routing number so the check hits the owner's account
                space_owner[1] = owner_balance + rent

            if current_player_balance <= self._board_spaces[board_number][1]:

                space_owner[1] = owner_balance + current_player_balance
                self._players[user_name][1] = 0
                # remove player from active player list since they are now inactive
                self._active_players.remove(user_name)

                # since player is now bankrupt, time to remove their properties
                for ownership in range(1, 25):
                    if user_name == self._board_spaces[ownership][3]:
                        self._board_spaces[ownership][3] = None

    def check_game_over(self):
        """
        Checks list of active players where players have balances of more than 0. If the list has only one player left,
        the game is over. If there are more than 1 player still in the game, the function returns an empty string.
        """
        if len(self._active_players) == 1:
            return self._active_players[0]
        else:
            return ""
