
class Board:

    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def output_board(self) -> None:
        """ Output the current  board to the console. """

        print('===============')
        for row_num in range(len(self.board)):
            row_str = '|'
            for col_num in range(len(self.board[row_num])):
                row_str += '| ' + self.board[row_num][col_num] + ' '
            row_str += '||'
            print(row_str)
            if row_num < len(self.board) - 1:
                print('---------------')
        print('===============')

    def board_is_full(self):
        board = []
        for i in range(3):
            for j in range(3):
                board.append(self.board[i][j])

        if " " in board:
            return False
        else:
            return True

    def drop(self, column, line, player):

        if self.board[line][column] == " ":
            self.board[line][column] = player
            return True

        elif (self.board_is_full()) or (self.board[line][column] != " "):
            return False

    def check_the_winner(self, player):
        combo_h = [[], [], []]
        for i in range(3):
            for j in range(3):
                combo_h[i].extend(self.board[i][j])

        combo_v = [[], [], []]
        for i in range(3):
            for j in range(3):
                combo_v[i].extend(self.board[j][i])

        #  Diagonal check
        combo_d = [self.board[0][2], self.board[1][1], self.board[2][0]]
        combo_d1 = [self.board[0][0], self.board[1][1], self.board[2][2]]

        if ((combo_d[0] == player) and (combo_d[1] == player) and (combo_d[2] == player)) or \
                ((combo_d1[0] == player) and (combo_d1[1] == player) and (combo_d1[2] == player)):
            return f"{player} won! Yay! D"

        #  Vertical check

        for i in range(3):
            counter_v = 0
            for j in range(3):
                if combo_v[i][j] == player:
                    counter_v += 1

                elif combo_v[i][j] != player:
                    counter_v = 0

                if counter_v == 3:
                    return f"{player} won! Yay! V"

        # Horizontal check

        for i in range(3):
            counter_h = 0
            for j in range(3):

                if combo_h[i][j] == player:
                    counter_h += 1

                elif combo_h[i][j] != player:
                    counter_h = 0

                if counter_h == 3:
                    return f"{player} won! Yay! H"

    @staticmethod
    def play_game():

        game = Board()
        game.output_board()

        first_player = input("Player 1,choose a sign: ")
        while len(first_player) > 1:
            first_player = input("Player 1,choose a one-letter sign: ")

        second_player = input("Player 2, choose a sign: ")
        while len(second_player) > 1:
            second_player = input("Player 2,choose a one-letter sign: ")

        while first_player == second_player:
            second_player = input("Player 2, choose a different sign: ")

        while not game.board_is_full():

            column = input(f"{first_player}, select a column from 0 to 2: ")
            line = input(f"{first_player}, select a line from 0 to 2: ")

            while int(column) >= 3:
                column = input(f"{first_player}, select a correct column: ")
            while int(line) >= 3:
                line = input(f"{first_player}, select a correct line: ")

            if not game.drop(int(column), int(line), first_player):

                print(f"{first_player}, please choose a different position!")
                column_o = input(f"{first_player}, select a column from 0 to 2: ")
                line_o = input(f"{first_player}, select a line from 0 to 2: ")

                while int(column_o) >= 3:
                    column_o = input(f"{first_player}, select a correct column: ")
                while int(line_o) >= 3:
                    line_o = input(f"{first_player}, select a correct line: ")

                while not game.drop(int(column_o), int(line_o), first_player):

                    print(f"{first_player}, please choose a different position!")
                    column_o = input(f"{first_player}, select a column from 0 to 2: ")
                    line_o = input(f"{first_player}, select a line from 0 to 2: ")

                    while int(column_o) >= 3:
                        column_o = input(f"{first_player}, select a correct column: ")
                    while int(line_o) >= 3:
                        line_o = input(f"{first_player}, select a correct line: ")

                game.drop(int(column_o), int(line_o), first_player)

            else:
                game.drop(int(column), int(line), first_player)

            print(game.output_board())

            if game.check_the_winner(first_player):
                print(f"Congratulations,{first_player}! You won!")
                break

            elif game.board_is_full() and ((not game.check_the_winner(second_player))
                                           or (not game.check_the_winner(first_player))):
                print("No winner!")
                break

            column_x = input(f"{second_player}, select a column from 0 to 2: ")
            line_x = input(f"{second_player}, select a line from 0 to 2: ")

            while int(column_x) >= 3:
                column_x = input(f"{second_player}, select a correct column: ")
            while int(line_x) >= 3:
                line_x = input(f"{second_player}, select a correct line: ")

            if not game.drop(int(column_x), int(line_x), second_player):

                print(f"{second_player}, please choose a different position!")
                column_x1 = input(f"{second_player}, select a column from 0 to 2: ")
                line_x1 = input(f"{second_player}, select a line from 0 to 2: ")

                while int(column_x1) >= 3:
                    column_x1 = input(f"{second_player}, select a correct column: ")
                while int(line_x1) >= 3:
                    line_x1 = input(f"{second_player}, select a correct line: ")

                while not game.drop(int(column_x1), int(line_x1), second_player):

                    print(f"{second_player}, please choose a different position!")
                    column_x1 = input(f"{second_player}, select a column from 0 to 2: ")
                    line_x1 = input(f"{second_player}, select a line from 0 to 2: ")

                    while int(column_x1) >= 3:
                        column_x1 = input(f"{second_player}, select a correct column: ")
                    while int(line_x1) >= 3:
                        line_x1 = input(f"{second_player}, select a correct line: ")

                game.drop(int(column_x1), int(line_x1), second_player)

            else:  
                game.drop(int(column_x), int(line_x), second_player)

            print(game.output_board())

            if game.check_the_winner(second_player):
                print(f"Congratulations, {second_player}! You won!")
                break
            elif game.board_is_full() and (
                    (not game.check_the_winner(second_player)) or (not game.check_the_winner(first_player))):
                print("No winner!")
                break


s = Board()
s.play_game()
