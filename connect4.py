from __future__ import annotations


class Board:

    def __init__(self):
        self.board = [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "]]

    def output_board(self) -> None:
        """ Output the current Connect 4 board to the console. """

        print('===============================')
        for row_num in range(len(self.board)):
            row_str = '|'
            for col_num in range(len(self.board[row_num])):
                row_str += '| ' + self.board[row_num][col_num] + ' '
            row_str += '||'
            print(row_str)
            if row_num < len(self.board) - 1:
                print('-------------------------------')
        print('===============================')

    def play_piece(self, column: int, piece: str) -> bool or None:
        """
        Place a specified piece to the chosen column. Drop the piece to the bottom of a column if the column is
        empty. If not, then place the piece above the highest piece in the chose column
        :param column: column number that a player chooses
        :param piece: the symbol of a player
        :return: a boolean indicating if the column is not full
        """
        if self.board[0][column] != " ":
            return False
        else:
            if self.board[5][column] == " ":
                self.board[5][column] = piece

            elif self.board[5][column] != " " and self.board[4][column] == " ":
                self.board[4][column] = piece

            elif self.board[4][column] != " " and self.board[3][column] == " ":
                self.board[3][column] = piece

            elif self.board[3][column] != " " and self.board[2][column] == " ":
                self.board[2][column] = piece

            elif self.board[2][column] != " " and self.board[1][column] == " ":
                self.board[1][column] = piece

            elif self.board[1][column] != " " and self.board[0][column] == " ":
                self.board[0][column] = piece

    def is_full(self) -> bool:
        """
        Check if the board if full
        :return: a boolean indicating if the board is full or not
        """
        list1 = []
        for j in range(6):
            for i in range(7):
                element = self.board[j][i] != " "
                list1.append(element)  # we took all False and/or True and checked if our list contains any False
        if False in list1:
            return False
        else:
            return True

    def check_victor(self) -> str:
        """
        Call other helper functions to check who the winner is
        :return: the symbol of the winner or ' '  if there is no winner
        """
        if self.check_victor_v() == "O":
            return "O"
        elif self.check_victor_v() == "X":
            return "X"
        elif self.check_victor_h() == "O":
            return "O"
        elif self.check_victor_h() == "X":
            return "X"
        elif self.check_victor_d() == "O":
            return "O"
        elif self.check_victor_d() == "X":
            return "X"
        else:
            return " "

    def check_victor_h(self) -> str:
        """
        Take all the values of all the rows to a new 2D list.
        Check if any list in 2D list has 4 consecutive identical symbols.
        :return: the symbol of the player or ' ' if there is no winner
        """
        combo = [[], [], [], [], [],
                 []]  # we are creating an empty 2D list to which we will add all the values in horizontal rows
        for i in range(7):
            for j in range(6):
                s = self.board[j][i]
                combo[j].append(s)

        counter1 = 0
        counter2 = 0

        for i in range(6):
            counter1 = 0
            counter2 = 0
            for j in range(7):

                if combo[i][j] == 'O':

                    counter1 += 1
                    counter2 = 0

                    if counter1 == 4:  # if the consecutive chain of Os reach, it returns "O" indicating that the
                        # player won
                        return "O"

                elif combo[i][j] == 'X':
                    counter1 = 0
                    counter2 += 1

                    if counter2 == 4:
                        return "X"
                elif combo[i][j] == " ":
                    counter1 = 0  # everytime an empty string is detected the consecutive chain breaks
                    counter2 = 0
        if counter2 or counter1 <= 4:
            return " "

    def check_victor_v(self) -> str:
        """
        Take all the values of all the columns to a new 2D list. Check if any list in 2D list has 4 consecutive
        identical symbols :return: the symbol of the player or ' ' if there is no winner
        """
        combo = [[], [], [], [], [], [], []]

        for i in range(6):
            for j in range(7):
                s = self.board[i][j]
                combo[j].append(s)
        counter1 = 0
        counter2 = 0
        for j in range(7):
            counter1 = 0
            counter2 = 0
            for i in range(6):

                if combo[j][i] == 'O':

                    counter1 += 1
                    counter2 = 0

                    if counter1 == 4:
                        return "O"

                elif combo[j][i] == 'X':
                    counter1 = 0
                    counter2 += 1

                    if counter2 == 4:
                        return "X"
                elif combo[j][i] == ' ':
                    counter1 = 0
                    counter2 = 0
        if counter2 or counter1 <= 4:
            return " "

    def check_victor_d(self) -> str:
        """
        Take all the possible diagonal combinations and check if they match any other that is on the board
        :return: the symbol of the player or ' ' if there is not winning diagonal combination
        """
        # we hard coded all possible diagonal winning combinations
        a = [self.board[2][0],
             self.board[3][1],
             self.board[4][2],
             self.board[5][3]]
        b = [self.board[1][0],
             self.board[2][1],
             self.board[3][2],
             self.board[4][3]]
        c = [self.board[2][1],
             self.board[3][2],
             self.board[4][3],
             self.board[5][4]]
        d = [self.board[0][0],
             self.board[1][1],
             self.board[2][2],
             self.board[3][3]]
        e = [self.board[1][1],
             self.board[2][2],
             self.board[3][3],
             self.board[4][4]]
        f = [self.board[2][2],
             self.board[3][3],
             self.board[4][4],
             self.board[5][5]]
        g = [self.board[0][1],
             self.board[1][2],
             self.board[2][3],
             self.board[3][4]]
        h = [self.board[1][2],
             self.board[2][3],
             self.board[3][4],
             self.board[4][5]]
        i = [self.board[2][3],
             self.board[3][4],
             self.board[4][5],
             self.board[5][6]]
        j = [self.board[0][2],
             self.board[1][3],
             self.board[2][4],
             self.board[3][5]]
        k = [self.board[1][3],
             self.board[2][4],
             self.board[3][5],
             self.board[4][6]]
        l = [self.board[0][3],
             self.board[1][4],
             self.board[2][5],
             self.board[3][6]]
        m = [self.board[2][6],
             self.board[3][5],
             self.board[4][4],
             self.board[5][3]]
        n = [self.board[1][6],
             self.board[2][5],
             self.board[3][4],
             self.board[4][3]]
        z = [self.board[2][5],
             self.board[3][4],
             self.board[4][3],
             self.board[5][2]]
        x = [self.board[0][6],
             self.board[1][5],
             self.board[2][4],
             self.board[3][3]]
        v = [self.board[1][5],
             self.board[2][4],
             self.board[3][3],
             self.board[4][2]]
        o = [self.board[2][4],
             self.board[3][3],
             self.board[4][2],
             self.board[5][1]]
        p = [self.board[0][5],
             self.board[1][4],
             self.board[2][3],
             self.board[3][2]]
        r = [self.board[1][4],
             self.board[2][3],
             self.board[3][2],
             self.board[4][1]]
        t = [self.board[2][3],
             self.board[3][2],
             self.board[4][1],
             self.board[5][0]]
        u = [self.board[0][4],
             self.board[1][3],
             self.board[2][2],
             self.board[3][1]]
        s = [self.board[1][3],
             self.board[2][2],
             self.board[3][1],
             self.board[4][0]]
        w = [self.board[0][3],
             self.board[1][2],
             self.board[2][1],
             self.board[3][0]]
        combo = [a, b, c, d, e, f, g, h, i, j, k, l, w, s, u, t, r, p, o, v, x, z, n,
                 m]  # created a 2D and checked if any list of 4 inside of the main list equals correct combinations of 4 Xs or 4 Os

        for j in range(24):

            list_y = ["O", "O", "O", "O"]
            list_x = ["X", "X", "X", "X"]
            if combo[j] == list_x:
                return "X"
            elif combo[j] == list_y:
                return "O"

        return " "


def play_game() -> str or None:
    """
    Initiate the game that continues until a player wins or the board is full
    :return: the symbol of the player who won the game or display that the game is a draw
    """
    print('Welcome to CS127 Connect 4!')
    print('The first player is O. The second is X.')
    print('Each player will pick a column from 0 to 6 each turn.')
    board = Board()
    board.output_board()

    # it will continue as long as the board is not full and no player has won
    while board.is_full() == False and board.check_victor() == " ":

        player1 = (int(input("Player 1(O). Column:")))

        # if the chosen column is full, the player is asked to choose a different column
        while not board.play_piece(int(player1), "O"):
            print("The column is full, try again")

            player1 = int(input("Player 1(O). Column:"))

        board.output_board()

        if board.check_victor() == "O":
            print("O won")
            break

        player2 = int(input("Player 2(X). Column:"))

        while not board.play_piece(int(player2), "X"):
            print("The column is full, try again")

            player2 = int(input("Player 2(X). Column:"))

        board.output_board()

        if board.check_victor() == "X":
            print("X won")
            break

    if board.is_full():
        print("No winner!")
        return


play_game()
