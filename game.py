import board as game_board
import player as game_player


class Game():

    def __init__(self):
        # Welcome message:
        print("\n*****************************************\n"
              "     Welcome to the TIC TAC TOE game\n"
              "*****************************************\n")

        # Initialize game board:
        self.board = game_board.Board()

        # Initialize players by game mode:
        self.__game_mode = self.__get_game_mode()
        if self.__game_mode == "PVP":
            # Player 1
            print("Enter data for PLAYER ONE!")
            self.player_1 = game_player.Player()
            self.player_1.set_player_name()
            self.player_1.set_player_mark()
            # Player 2
            print("\nEnter data for PLAYER TWO!")
            self.player_2 = game_player.Player()
            self.player_2.set_player_name()
            self.player_2.set_player_mark(self.player_1.get_mark())
        elif self.__game_mode == "PVAI":
            # Player 1
            print("Enter data for PLAYER ONE!")
            self.player_1 = game_player.Player()
            self.player_1.set_player_name()
            self.player_1.set_player_mark()
            # Player 2
            ai_difficulty = self.__get_ai_difficulty()
            self.player_2 = self.__get_ai_player_by_difficulty(ai_difficulty)
            self.player_2.set_player_mark(self.player_1.get_mark())

            if self.player_2.get_difficulty() == "HARD":
                self.player_2.set_opponent_mark(self.player_1.get_mark())
        elif self.__game_mode == "AIVAI":
            # Player 1
            print("Initialize AI player ONE: ")
            ai_difficulty = self.__get_ai_difficulty()
            self.player_1 = self.__get_ai_player_by_difficulty(ai_difficulty)
            self.player_1.set_name(self.player_1.get_fun_name())
            self.player_1.set_player_mark(game_player.Player.MARKS[0])
            # Player 2
            print("\nInitialize AI player TWO: ")
            ai_difficulty = self.__get_ai_difficulty()
            self.player_2 = self.__get_ai_player_by_difficulty(ai_difficulty)
            self.player_2.set_name(
                self.player_2.get_fun_name(self.player_1.get_name()))
            self.player_2.set_player_mark(self.player_1.get_mark())

            if self.player_1.get_difficulty() == "HARD":
                self.player_1.set_opponent_mark(self.player_2.get_mark())
            if self.player_2.get_difficulty() == "HARD":
                self.player_2.set_opponent_mark(self.player_1.get_mark())
        else:
            print("ERROR! Not a valid game mode!")

    def __get_ai_player_by_difficulty(self, difficulty):
        if difficulty == "EASY":
            return game_player.Easy_Ai_Player()
        elif difficulty == "HARD":
            return game_player.Hard_Ai_Player()
        else:
            print("ERROR! Not a valid AI difficulty")
            return None

    def __get_game_mode(self):
        GAME_MODES = {
            "1": "PVP",
            "2": "PVAI",
            "3": "AIVAI"
        }
        game_mode = input("Select game mode:\n"
                          "     Press 1 for PLAYER vs. PLAYER\n"
                          "     Press 2 for Player vs. AI\n"
                          "     Press 3 for AI vs AI: \n")
        while game_mode not in GAME_MODES:
            game_mode = input("Not a valid input! Try again: ")
        return GAME_MODES[game_mode]

    def __get_ai_difficulty(self):
        DIFFICULTIES = {
            "1": "EASY",
            "2": "HARD"
        }
        difficulty = input("Select difficulty:\n"
                           "    Press 1 for EASY\n"
                           "    Press 2 for HARD:\n")
        while difficulty not in DIFFICULTIES:
            difficulty = input("Not a valid input! Try again: ")
        return DIFFICULTIES[difficulty]

    def __handle_turn(self, player, board):
        print(f"It is your turn {player.get_name()}!")
        board.display_board()
        player.make_move(board)
        game_won = board.is_game_won()
        return game_won

    def __get_player_info(self, player):
        info = (f"Player name: {player.get_name()}\n"
                f"Player mark: {player.get_mark()}\n")
        if isinstance(player, game_player.Easy_Ai_Player) or isinstance(player, game_player.Hard_Ai_Player):
            info += f"AI player difficulty: {player.get_difficulty()}"
        return info

    def play_game(self):
        print("*****************************************\n"
              "               GAME STARTED!\n"
              "*****************************************")
        print(self.__get_player_info(self.player_1))
        print(self.__get_player_info(self.player_2))
        game_over = False
        turn = 0
        while not game_over:
            print(f"************** TURN_{turn} **************")
            for player in (self.player_1, self.player_2):
                player_won = self.__handle_turn(player, self.board)
                draw = self.board.is_game_draw()
                if draw:
                    print("************** DRAW **************")
                    self.board.display_board()
                    print(f"It is a DRAW!")
                    game_over = True
                    break
                if player_won:
                    print("************** WINNER **************")
                    self.board.display_board()
                    print(
                        f"CONGRATULATIONS {player.get_name()} you have won the game!")
                    game_over = True
                    break
            turn += 1
        print("*****************************************")


if __name__ == "__main__":
    new_game = Game()
    new_game.play_game()

"""
TODO: 
    3. Refactor Code and Test
    4. Do GUI APP
    5. DO WEB APP with React
"""
