import random


class Player():
    # valid marks for the player:
    MARKS = ("X", "O")

    def __init__(self):
        self.__name = ""
        self.__mark = ""

    def __get_move(self, col_or_row):
        move = input(f"Select {col_or_row}: ")
        while not move.isdigit():
            move = input("ERROR! Try again:!\n"
                         f"Select {col_or_row}: ")
        return int(move)

    def __get_moves(self):
        row = self.__get_move("ROW")
        column = self.__get_move("COLUMN")
        return {
            "ROW": row,
            "COLUMN": column
        }

    def make_move(self, board):
        move = self.__get_moves()
        is_move_succesful = board.modify_position(move["ROW"],
                                                  move["COLUMN"],
                                                  self.get_mark())
        while not is_move_succesful:
            print("ERROR! Not a valid move.")
            move = self.__get_moves()
            is_move_succesful = board.modify_position(move["ROW"],
                                                      move["COLUMN"],
                                                      self.get_mark())

    # Value getters:
    def get_name(self):
        return self.__name

    def get_mark(self):
        return self.__mark

    # Value setters:
    def set_player_name(self, other_player_name=""):
        self.__name = input("Enter a name: ").upper().strip()
        if other_player_name != "":
            while self.__name == other_player_name.upper().strip():
                self.__name = input("ERROR! Identical names! Try again: ")

    def set_player_mark(self, first_player_mark=""):
        if first_player_mark == "":
            self.__mark = input(
                f"Press {Player.MARKS[0]} or {Player.MARKS[1]} to select a mark: ").upper()
            while self.__mark not in Player.MARKS:
                self.__mark = input("Not a valid mark! Try again: ").upper()
        else:
            if first_player_mark == Player.MARKS[0]:
                self.__mark = Player.MARKS[1]
            else:
                self.__mark = Player.MARKS[0]


class Ai_Player(Player):

    NAMES = [
        "Bence_AI",
        "Szivike_AI"
    ]

    def __init__(self):
        super().__init__()

    def get_fun_name(self, other_player_name=""):
        return random.choice([name for name in Ai_Player.NAMES if name != other_player_name])

# Makes a move to random empty field in the board


class Easy_Ai_Player(Ai_Player):

    DIFFICULTY = "EASY"

    def __init__(self):
        self.__name = self.DIFFICULTY + "_AI"
        self.__difficulty = Easy_Ai_Player.DIFFICULTY

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_difficulty(self):
        return self.__difficulty

    def make_move(self, board):
        temp = []
        for row in range(board.get_rows()):
            for col in range(board.get_cols()):
                if board.get_board()[row][col] == board.get_empty_field_mark():
                    temp.append([row, col])
        ai_move = random.choice(temp)

        board.modify_position(ai_move[0],
                              ai_move[1],
                              self.get_mark())

# MINI MAX algorithm with pruning:


class Hard_Ai_Player(Ai_Player):

    DIFFICULTY = "HARD"

    def __init__(self):
        self.__name = self.DIFFICULTY + "_AI"
        self.__difficulty = Hard_Ai_Player.DIFFICULTY
        self.__player_mark = Player().get_mark()
        self.__opponent_mark = ""

    def set_opponent_mark(self, opponent_mark):
        self.__opponent_mark = opponent_mark

    def get_difficulty(self):
        return self.__difficulty

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def minimax(self, board, depth, alpha, beta, is_max):
        if is_max and board.is_game_won():
            score = -10
        elif not is_max and board.is_game_won():
            score = 10
        else:
            score = 0

        if score == 10 or score == -10:
            return score

        if board.is_game_draw():
            return 0

        if is_max:
            best = -1000
            for row in range(board.get_rows()):
                for col in range(board.get_cols()):
                    if (board.get_board()[row][col] == board.get_empty_field_mark()):
                        board.get_board()[row][col] = self.__player_mark
                        best = max(best, self.minimax(board,
                                                      depth + 1,
                                                      alpha,
                                                      beta,
                                                      not is_max))
                        alpha = max(alpha, best)
                        board.get_board()[
                            row][col] = board.get_empty_field_mark()
                        if beta <= alpha:
                            break
            return best
        else:
            best = 1000
            for row in range(board.get_rows()):
                for col in range(board.get_cols()):
                    if board.get_board()[row][col] == board.get_empty_field_mark():
                        board.get_board()[row][col] = self.__opponent_mark
                        best = min(best, self.minimax(board,
                                                      depth + 1,
                                                      alpha,
                                                      beta,
                                                      not is_max))
                        beta = min(beta, best)
                        board.get_board()[
                            row][col] = board.get_empty_field_mark()
                        if beta <= alpha:
                            break
            return best

    def findBestMove(self, board):
        bestVal = -1000
        bestMove = (-1, -1)
        for row in range(board.get_rows()):
            for col in range(board.get_cols()):
                if board.get_board()[row][col] == board.get_empty_field_mark():
                    board.get_board()[row][col] = self.__player_mark
                    moveVal = self.minimax(board, 0, 0, 0, False)
                    board.get_board()[row][col] = board.get_empty_field_mark()
                    if moveVal > bestVal:
                        bestMove = (int(row), int(col))
                        bestVal = int(moveVal)
        return bestMove

    def make_move(self, board):
        bestmove = self.findBestMove(board)
        board.modify_position(bestmove[0],
                              bestmove[1],
                              self.get_mark())
