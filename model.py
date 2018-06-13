

class Cell:

    """
    This class contains the whole logic of a unique Cell
    Attributes:
    value: Integer which contains the current value, it can only be modified once
    """
    def __init__(self, new_value):
        self.value = new_value

    def __str__(self):
        if(self.value is -1):
            return ""
        else:
            return str(self.value)

class Board:
    """
    This class contains the whole logic of the game board
    Attributes:
    _board: 9x9 matrix of Cell
    __rows_size: Integer which defines the x-dimension
    __columns_size: Integer which defines the y-dimension
    row_picks_list: Lists for every row (rows_size) a list of 9 booleans indicating which elements have been used in that row
    row_picks_count: Enumerates for every row how many elements have been selected in that row
    column_picks_list: Lists for every column (columns_size) a list of 9 booleans indicating which elements have been used in that row
    column_picks_count: Enumerates for every column how many elements have been selected in that column
    __initial_picks_size: Integer which defines how many picks are randomly generated at the beginning of each game
    """

    def __init__(self):
        self.__rows_size = 9
        self.__columns_size = 9
        self.__initial_picks_size = 30
        self.row_picks_list = [False for i in range(self.__rows_size)]
        self.row_picks_count = 0
        self.column_picks_list = [False for i in range(self.__columns_size)]
        self.column_picks_count = 0
        self.init_board()

    def init_board(self):
        pass ##todo