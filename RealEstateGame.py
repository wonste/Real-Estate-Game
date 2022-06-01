# Author: Stella Wong
# GitHub username: wonste
# Date: 06/03/22
# Description: The program is a very simplified version of Monopoly. The program will only allow for players to roll a
# single die (from 1 to 6) and moving across the board in a circular motion. There is no Jail but there are properties to
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

        self._active_players.append(user_name)
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
        Function takes in the player's name and value they "rolled" the dice to move the player forward on the game
        board. The location they land in determines whether the player will pay, earn, or idle depending on their
        conditions. Due to requirements, this is probably the longest and most convoluted method.
        """
        person = self._players[user_name]
        player_balance = person.get_player_account_balance()
        player_position = person.get_player_position()

        if player_balance == 0:
            # If the player's account balance is 0, the method will return immediately without doing anything
            return

        # dice roll ranges from 1 to 6
        if 6 <= travel_amount >= 1:
            player_position += travel_amount

            if player_position > 24:
                # players who pass
                player_balance += self._board_spaces[0][1]

                if player_position == 25:
                    # reset player position so player is at GO
                    player_position = 0

                if player_position > 25:
                    # reduce to be within board space range
                    player_position -= 25

                    for board_number in self._board_spaces:

                        if player_position == board_number:

                            if self._board_spaces[board_number][3] is not None:

                                if self._board_spaces[board_number][3] is not user_name:

                                    for landlord in self._players:

                                        if landlord == self._players[self._board_spaces[3]]:
                                            rent = self._board_spaces[board_number][1]

                                            if player_balance > self._board_spaces[board_number][1]:
                                                player_balance -= rent
                                                pay_rent = self.get_player_account_balance(landlord)
                                                pay_rent += rent

                                            if player_balance <= self._board_spaces[board_number][1]:
                                                pay_rent = self.get_player_account_balance(landlord)
                                                pay_rent += player_balance
                                                player_balance = 0
                                                self._active_players.remove(user_name)


        else:
            return

    def check_game_over(self):
        """
        Checks every player's balance to see if the game is done. If there is only 1 player with a balance not at 0,
        the game is over and that player is declared the winner. If there's no winner, the function will return an empty
        string.
        """

        if len(self._active_players) == 1:
            return self._active_players
        else:
            return ""
