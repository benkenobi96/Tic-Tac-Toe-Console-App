class Board():
    BOARD_ROWS = 3
    BOARD_COLS = 3
    EMPTY_FIELD_MARK = "_"

    def __init__(self, rows=BOARD_ROWS, cols=BOARD_COLS, empty_field_mark=EMPTY_FIELD_MARK):
        self.__rows = rows
        self.__cols = cols
        self.__empty_field_mark = empty_field_mark
        self.__board = []
        self.__initialize_board()

    def __initialize_board(self):
        rec = []
        for col in range(self.__cols):
            rec.append(self.__empty_field_mark)
        for row in range(self.__rows):
            # needs the list() method, otherwise it is the same object appended 3 times
            self.__board.append(list(rec))

    # Value getters:
    def get_board(self):
        return self.__board

    def get_rows(self):
        return self.__rows

    def get_cols(self):
        return self.__cols

    def get_empty_field_mark(self):
        return self.__empty_field_mark

    def display_board(self):
        for row in range(self.__rows):
            for col in range(self.__cols):
                print(self.__board[row][col], end="|" if col != len(
                    self.__board[row])-1 else "")
            print()

    # modifies a position on the board
    def modify_position(self, row, column, mark):
        if self.__is_move_valid(row, column):
            self.__board[row][column] = mark
            return True
        else:
            return False

    # check game win:
    def __check_diagonals(self):
        game_won = False
        temp = []
        for row in range(self.__rows):
            temp.append(str(self.__board[row][row]))
        if len(set(temp)) == 1 and temp[0] != Board.EMPTY_FIELD_MARK:
            game_won = True

        temp = []
        for row in range(self.__rows):
            temp.append(str(self.__board[row][self.__rows-1-row]))
        if len(set(temp)) == 1 and temp[0] != Board.EMPTY_FIELD_MARK:
            game_won = True
        return game_won

    def __check_rows(self):
        game_won = False
        # check rows
        for row in self.__board:
            if len(set(row)) == 1 and row[0] != Board.EMPTY_FIELD_MARK:
                game_won = True
        return game_won

    def __check_cols(self):
        game_won = False
        for col in range(self.__rows):
            temp = []
            for row in range(self.__cols):
                temp.append(str(self.__board[row][col]))
            if len(set(temp)) == 1 and temp[0] != Board.EMPTY_FIELD_MARK:
                game_won = True
        return game_won

    def is_game_won(self):
        return any([self.__check_cols(), self.__check_diagonals(), self.__check_rows()])

    def is_game_draw(self):
        empty_cnt = 0
        for row in range(self.__rows):
            for col in range(self.__cols):
                if self.__board[row][col] == self.__empty_field_mark:
                    empty_cnt += 1
        return True if empty_cnt == 0 else False

    def __is_move_valid(self, row, column):
        # check if move is list indexes
        if (row > self.__rows - 1 or row < 0) or (column > self.__cols - 1 or column < 0):
            return False
        else:
            # check if target field is empty
            if self.__board[row][column] == Board.EMPTY_FIELD_MARK:
                return True
            else:
                return False
