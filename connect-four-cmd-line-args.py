import numpy as np
import argparse as arg


class ConnectFour:

    def __init__(self, rows: int, columns: int, player_1_choice: str, player_2_choice: str, pieces: int):

        # Get board size
        self.ROWS = rows
        self.COLUMNS = columns

        # Get Player colors
        self.PLAYER_1_CHOICE = player_1_choice
        self.PLAYER_2_CHOICE = player_2_choice

        # Get winning pieces
        self.PIECES = pieces

        self.turn = 0
        self.GAME_OVER = False
        self.EMPTY = "-"

        # create board
        self.board = np.chararray((self.ROWS, self.COLUMNS), unicode=True)
        self.board[:] = self.EMPTY

    def check_if_valid_move(self, column):
        return self.board[self.ROWS - 1][column] == self.EMPTY

    def get_location_to_add_piece(self, column):

        for row in range(self.ROWS):
            if self.board[row][column] == self.EMPTY:
                return row

    def show(self):
        print("\n\n")
        print(np.flip(self.board, axis=0))
        print("\n\n")

    def check_if_player_won(self, piece):

        # for row elements checking
        for r in range(self.ROWS):
            for c in range(self.COLUMNS - (self.PIECES - 1)):
                sub_section = self.board[r][c:c+self.PIECES]
                if np.all(sub_section == piece):
                    return True

        # for column elements checking  # print(board[:ROWS-(PIECES-1), :])
        for r in range(self.ROWS - (self.PIECES - 1)):
            for c in range(self.COLUMNS):
                sub_section = self.board[r:r+self.PIECES, c]
                if np.all(sub_section == piece):
                    return True

        # for diagonal elements checking
        for r in range(self.ROWS - (self.PIECES - 1)):
            for c in range(self.COLUMNS - (self.PIECES - 1)):
                sub_section = self.board[r:r+self.PIECES, c:c+self.PIECES]
                diagonal_elements_left = sub_section.diagonal()
                diagonal_element_right = np.fliplr(sub_section).diagonal()

                if np.all(diagonal_elements_left == piece):
                    return True

                if np.all(diagonal_element_right == piece):
                    return True

        return False

    def start(self):

        # Start the Game
        self.show()

        while not self.GAME_OVER:

            # ask player 1 input
            if self.turn == 0:

                try:
                    choice = (
                        int(input(f"\n\nPlayer 1 make your selection (1-{self.COLUMNS}): ")) - 1)

                    if not (choice >= 0 and choice < self.COLUMNS):
                        raise ValueError("Wrong Choice")
                except ValueError as e:
                    print("Wrong Choice!")
                    break

                if self.check_if_valid_move(choice):
                    row = self.get_location_to_add_piece(choice)

                    self.board[row][choice] = self.PLAYER_1_CHOICE

                    if self.check_if_player_won(self.PLAYER_1_CHOICE):
                        self.show()

                        print("---------------------------------")
                        print(f"\nPlayer 1 ({self.PLAYER_1_CHOICE}) won.\n")
                        print("---------------------------------")
                        exit()

            # ask player 2 input
            else:

                try:
                    choice = (
                        int(input(f"\n\nPlayer 2 make your selection (1-{self.COLUMNS}): ")) - 1)

                    if not (choice >= 0 and choice < self.COLUMNS):
                        raise ValueError("Wrong Choice")

                except ValueError as e:
                    print("Wrong Choice!")
                    break

                if self.check_if_valid_move(choice):
                    row = self.get_location_to_add_piece(choice)

                    self.board[row][choice] = self.PLAYER_2_CHOICE

                    if self.check_if_player_won(self.PLAYER_2_CHOICE):
                        self.show()
                        print("---------------------------------")
                        print(f"\nPlayer 2  ({self.PLAYER_2_CHOICE})  won.\n")
                        print("---------------------------------")
                        exit()

            self.show()
            self.turn += 1
            self.turn = self.turn % 2


print("Welcome to Game of Connect Four\n")


if __name__ == "__main__":
    parser = arg.ArgumentParser(description="Connect 4 Game")
    parser.add_argument("-r", "--row", type=int, default=6,
                        help="Number of Rows")
    parser.add_argument("-c", "--column", type=int,
                        default=7, help="Number of Columns")
    parser.add_argument("-p", "--pieces", type=int, default=4,
                        help="Number of Pieces to win")
    parser.add_argument("-p1", "--player1_color", type=str,
                        default='r', help="Player 1 Color")
    parser.add_argument("-p2", "--player2_color", type=str,
                        default='y', help="Player 2 Color")
    args = parser.parse_args()

    ROWS = args.row
    COLUMNS = args.column
    PIECES = args.pieces
    PLAYER_1_CHOICE = args.player1_color
    PLAYER_2_CHOICE = args.player2_color

    if ROWS < 1:
        print("Number of rows cannot be less then 1")
        exit()

    if COLUMNS < 1:
        print("Number of columns cannot be less then 1")
        exit()

    if PIECES < 1 or (PIECES > ROWS and PIECES > COLUMNS):
        print("Pieces cannot be less then 1 and greater rows and columns")
        exit()

    game = ConnectFour(ROWS, COLUMNS, PLAYER_1_CHOICE, PLAYER_2_CHOICE, PIECES)
    game.start()
