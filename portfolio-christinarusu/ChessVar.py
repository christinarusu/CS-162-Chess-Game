# Author: Christina Rusu
# GitHub username: christinarusu
# Date: 12/9/2024
# Description: a program that designs an abstract board game based on a chess variant known as Fog of War chess.

class ChessVar:
    """A class representing a chess board game with methods that set up the rules and flow of the game."""
    def __init__(self):
        """Creates a ChessVar chess board game with a game state, board, and turn.
         Initializes the required data members. All data members are private."""
        self._game_state = "UNFINISHED"
        self._board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                       ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                       ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
        self._turn = "white"

    def get_game_state(self):
        """returns the game state of the ChessVar game"""
        return self._game_state

    def set_game_state(self, state):
        """sets the game state to a new status"""
        self._game_state = state

    def set_turn(self, turn):
        """sets the turn to a new player"""
        self._turn = turn

    def change_turn(self):
        """Calculates which player's turn it is, depending on whose turn it currently is. Alternates turns between
        white and black"""
        if self._turn == "white":
            self.set_turn("black")
        else:
            self.set_turn("white")  # accounts for white going first

    def valid_turn(self, chess_piece):
        """
        Calculates: whether the current turn is correct to ensure that a player moves their chess pieces and does not
                    go twice in a row
        Parameter: chess_piece-- the chess piece being moved on this turn
        Returns: a True or False value depending on whether the turn is correct and the player is moving their
                 corresponding chess piece
        """
        if self._turn == "white" and chess_piece == chess_piece.upper():  # condition for white player turn
            return True
        elif self._turn == "black" and chess_piece == chess_piece.lower():  # condition for black player turn
            return True
        else:
            return False

    def move_rules(self, from_row, from_col, to_row, to_col):
        """
        Calculates: the valid moves for each piece based on chess game rules
        Parameter: from_row-- the row from where the piece will move
        Parameter: from_col-- the column from where the piece will move
        Parameter: to_row-- the row to which the piece will move
        Parameter: to_col-- the column to which the piece will move
        Returns: a True value if the piece moves to a valid spot. A False value if the piece moves to an invalid space.
        """
        row = abs(to_row - from_row)  # the difference between to_row and from_row
        column = abs(to_col - from_col)  # the difference between the to_col and from_col
        begin_piece = self._board[from_row][from_col]
        end_piece = self._board[to_row][to_col]
        if begin_piece == ' ':  # if move_from spot is empty and does not have a piece to be moved returns False
            return False
        if end_piece != ' ':
            if begin_piece == begin_piece.upper() and end_piece == end_piece.upper():  # white can't capture white piece
                return False
            if begin_piece == begin_piece.lower() and end_piece == end_piece.lower():  # black can't capture black piece
                return False
        if begin_piece == 'P' or begin_piece == 'p':  # rules for how a pawn moves including 2 spaces for 1st move
            raw_val_row = from_row - to_row
            if end_piece == ' ':  # if pawn in moving to empty space
                if begin_piece == 'P' and from_row == 6 and row == 2 and column == 0:  # 2 spaces
                    return True
                elif begin_piece == 'p' and from_row == 1 and row == 2 and column == 0:  # 2 spaces
                    return True
                elif raw_val_row == 1 and begin_piece == 'P' and column == 0:  # white pawns moving forward one space
                    return True
                elif raw_val_row == -1 and begin_piece == 'p' and column == 0:  # black pawns moving forward one space
                    return True
            if end_piece != ' ':  # if pawn is capturing
                if row == column:  # accounts for diagonal capture of piece by a pawn
                    if (begin_piece == 'P') and (raw_val_row == 1) and (end_piece == end_piece.lower()):
                        return True
                    elif (begin_piece == 'p') and (raw_val_row == -1) and (end_piece == end_piece.upper()):
                        return True
            else:
                return False
        if begin_piece == 'R' or begin_piece == 'r':  # rules for how a rook moves
            if row == 0 or column == 0:  # if move is either horizontal or vertical
                if from_row == to_row:  # if move is horizontal
                    if to_col > from_col:
                        step = 1
                    else:
                        step = -1
                    for val in range(from_col + step, to_col, step):
                        if self._board[from_row][val] != ' ':  # makes sure path between columns is clear
                            return False
                    return True
                elif from_col == to_col:  # if move is vertical
                    if to_row > from_row:
                        step = 1
                    else:
                        step = -1
                    for var in range(from_row + step, to_row, step):
                        if self._board[var][from_col] != ' ':  # makes sure path between rows is clear
                            return False
                    return True
                else:
                    return True
            return False  # returns false if move is diagonal
        if begin_piece == 'N' or begin_piece == 'n':  # rules for how a knight moves
            if row == 2 and column == 1 or row == 1 and column == 2:  # ensures knight can only move in L shape
                return True
            else:
                return False
        if begin_piece == 'B' or begin_piece == 'b':  # rules for how bishop moves
            if row == column:  # if move is diagonal
                if to_row > from_row:
                    row_index = 1
                else:
                    row_index = -1
                if to_col > from_col:
                    col_index = 1
                else:
                    col_index = -1
                row_1 = from_row + row_index
                col_1 = from_col + col_index
                while row_1 != to_row and col_1 != to_col:
                    if self._board[row_1][col_1] != ' ':
                        return False
                    row_1 += row_index
                    col_1 += col_index
                return True
            else:
                return False  # returns false if move is not diagonal
        if begin_piece == 'Q' or begin_piece == 'q':  # rules for how a queen moves. Rook + bishop is how queen moves.
            if from_row == to_row:
                if to_col > from_col:
                    step = 1
                else:
                    step = -1
                for val in range(from_col + step, to_col, step):
                    if self._board[from_row][val] != ' ':  # makes sure path between columns is clear
                        return False
            if from_col == to_col:
                if to_row > from_row:
                    step = 1
                else:
                    step = -1
                for val in range(from_row + step, to_row, step):
                    if self._board[val][from_col] != ' ':  # makes sure path between rows is clear
                        return False
            if row == column:  # employs the bishop rules and makes sure path is clear
                if to_row > from_row:
                    row_index = 1
                else:
                    row_index = -1
                if to_col > from_col:
                    col_index = 1
                else:
                    col_index = -1
                row_1 = from_row + row_index
                col_1 = from_col + col_index
                while row_1 != to_row and col_1 != to_col:
                    if self._board[row_1][col_1] != ' ':
                        return False
                    row_1 += row_index
                    col_1 += col_index
                return True
            if row == 0 or column == 0:  # ensures the queen can move any direction
                return True
            else:
                return False
        if begin_piece == 'K' or begin_piece == 'k':  # rules for how a king moves.
            if row == 1 and column == 0:  # ensures king only moves one space at a time in any direction
                return True
            if row == 0 and column == 1:
                return True
            if row == column:
                if row <= 1 or column <= 1:
                    return True
        return False

    def get_capture_pieces(self):
        """
        Calculates: the opponent's pieces on the board that can be captured within the next move
        returns: a list of indexes of opponent pieces that can be captured
        """
        pieces = []
        for row in range(0, 8):
            for col in range(0, 8):
                piece = self._board[row][col]
                if piece != ' ':  # if from piece isn't an empty space
                    for row_1 in range(0, 8):
                        for col_1 in range(0, 8):
                            if self.move_rules(row, col, row_1, col_1) is True and self._board[row_1][col_1] != ' ':
                                # if move_rules are met and the end piece isn't an empty space
                                pieces.append((row_1, col_1))  # adds board indexes to list to be used in get_board
        return pieces

    def get_board(self, board):
        """
        Calculates: a board depending on the perspective provided
        Parameter: board-- the perspective of the chess board ("white", "black", or "audience")
        returns: a version of the chess board with opponent's pieces blurred or entire chess board for audience view
        """
        display_board = []  # new list for board to be displayed
        if board == "audience":  # if board is audience view
            return self._board
        if board != "white" and board != "black":  # if board is anything besides "white" or "black"
            return False
        else:
            for val in range(0, 8):
                row = []
                for var in range(0, 8):
                    chess_piece = self._board[val][var]  # defines chess piece with indexes
                    if board == "white":
                        if chess_piece == ' ':
                            row.append(' ')  # adds empty spaces to row
                        elif (val, var) in self.get_capture_pieces():  # adds capturable opponent pieces to row
                            row.append(self._board[val][var])
                        elif chess_piece == chess_piece.upper():
                            row.append(chess_piece)  # adds white pieces to row
                        else:
                            row.append('*')  # adds * to blur all black pieces in row
                    if board == "black":
                        if chess_piece == ' ':
                            row.append(' ')  # adds empty spaces to row
                        elif (val, var) in self.get_capture_pieces():  # adds capturable opponent pieces to row
                            row.append(self._board[val][var])
                        elif chess_piece == chess_piece.lower():
                            row.append(chess_piece)  # adds black pieces to row
                        else:
                            row.append('*')  # adds * to blur all white pieces in row
                display_board.append(row)  # adds the rows together to create the board to be displayed
            return display_board  # returns entire board with pieces depending on view

    def make_move(self, move_from, move_to):
        """
        Calculates: the movement of a chess piece from one space to another
        Parameter: move_from-- the coordinate of the space the piece is moving from
        Parameter: move_to-- the coordinate of the space the move is moving to
        returns: the piece in the move_to spot, and resets the move_from space to ' '. Changes turn to next player.
        """
        chess_letter_dict = {'a': 0,  # a dictionary for the letter part of the coordinate.
                             'b': 1,  # key: letter, value: corresponding indexing sequence (0- 7)
                             'c': 2,
                             'd': 3,
                             'e': 4,
                             'f': 5,
                             'g': 6,
                             'h': 7}
        chess_num_dict = {'8': 0,  # a dictionary for the number part of the coordinate
                          '7': 1,  # key: number, value: corresponding indexing sequence (0- 7)
                          '6': 2,
                          '5': 3,
                          '4': 4,
                          '3': 5,
                          '2': 6,
                          '1': 7}
        if move_from[0] not in chess_letter_dict:  # if move_from letter is not on the board
            return False
        if move_from[1] not in chess_num_dict:  # if move_from number is not on the board
            return False
        if move_to[0] not in chess_letter_dict:  # if move_to letter is not on the board
            return False
        if move_to[1] not in chess_num_dict:  # if move_to number is not on the board
            return False
        for key_let in chess_letter_dict:
            for key_num in chess_num_dict:
                if move_from[0] == key_let and move_from[1] == key_num:  # assigns move_from coordinate to indexes
                    y_val = chess_letter_dict[key_let]  # assigns letter in coordinate to index
                    x_val = chess_num_dict[key_num]  # assigns number in coordinate to index
                    if not (0 <= y_val <= 7) and (0 <= x_val <= 7):  # if from indexes are not within range
                        return False
                    var = self._board[x_val][y_val]
                    for key_let_1 in chess_letter_dict:
                        for key_num_1 in chess_num_dict:
                            if move_to[0] == key_let_1 and move_to[1] == key_num_1:  # assigns move_to to indexes
                                y_val_1 = chess_letter_dict[key_let_1]  # assigns letter in coordinate to index
                                x_val_1 = chess_num_dict[key_num_1]  # assigns number in coordinate to index
                                if not (0 <= y_val_1 <= 7) and (0 <= x_val_1 <= 7):  # if to indexes aren't within range
                                    return False
                                if self.valid_turn(var) is False:  # if it is not the correct player's turn
                                    return False
                                if self.move_rules(x_val, y_val, x_val_1, y_val_1) is False:  # checks move_rules
                                    return False
                                if self.get_game_state() != "UNFINISHED":  # if game was won, move can't be made
                                    return False
                                if self._board[x_val_1][y_val_1] == 'k' and self._turn == "white":  # white won rules
                                    self.set_game_state('WHITE_WON')
                                    return self.get_game_state()
                                if self._board[x_val_1][y_val_1] == 'K' and self._turn == "black":  # black won rules
                                    self.set_game_state('BLACK_WON')
                                    return self.get_game_state()
                                else:
                                    self._board[x_val][y_val] = ' '  # clears the move_from space
                                    self._board[x_val_1][y_val_1] = var  # assigns chess piece to new move_to space
                                    self.change_turn()  # changes turn to next player

                    return True
