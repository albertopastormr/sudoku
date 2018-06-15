class ModelError(Exception):
    """ Wraps exceptions occured at the model for the legibility"""

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
    Logic of a sudoku game board
    Attributes:
    _board: 9x9 matrix of Cell
    _rows_size: Integer which defines the x-dimension
    _columns_size: Integer which defines the y-dimension
    row_picks_list: Lists for every row (_rows_size) a list of 9 booleans indicating which elements have been used in that row
    row_picks_count: Enumerates for every row how many elements have been selected in that row
    column_picks_list: Lists for every column (_columns_size) a list of 9 booleans indicating which elements have been used in that column
    column_picks_count: Enumerates for every column how many elements have been selected in that column
    square_picks_list: Lists for every square (_squares_size) a list of 9 booleans indicating which elements have been used in that square
    square_picks_count: Enumerates for every square how many elements have been selected in that square
    _initial_picks_size: Integer which defines how many picks are randomly generated at the beginning of each game
    """

    def __init__(self):
        self._rows_size = 9
        self._columns_size = 9
        self._squares_size = 9
        self._initial_picks_size = 30
        self.row_picks_list = [False for i in range(self._rows_size)]
        self.row_picks_count = [0 for i in range(self._rows_size)]
        self.column_picks_list = [False for i in range(self._columns_size)]
        self.column_picks_count = [0 for i in range(self._columns_size)]
        self.square_picks_list = [False for i in range(self._squares_size)]
        self.square_picks_count = [0 for i in range(self._squares_size)]
        self.init_board()

    def init_board(self):
        # to-do
        for i in range(self._initial_picks_size):
            pass

    def place_element(self, x_index, y_index, elem):
        """
        Place the object 'elem' at the intersection x-y received by argument.
        Throws ModelError(user row-column-square counting) if it could not be completed.
        """
    
        if(x_index >= self._rows_size or x_index < 0 or y_index >= self._columns_size or y_index < 0):
            raise ModelError("row or column selection out of range (x:{},y:{})".format(x_index, y_index))
        if(self.row_picks_list[x_index][elem]):
            raise ModelError("element {} already in use in the selected row {}".format(elem, x_index + 1))
        if(self.column_picks_list[y_index][elem]):
            raise ModelError("element {} already in use in the selected column {}".format(elem, x_index + 1))
        square_index = self.get_square_index(x_index,y_index)
        if(self.square_picks_list[square_index][elem]):
            raise ModelError("element {} already in use in the square {}".format(elem, square_index + 1))
        
        self.row_picks_list[x_index][elem] = True
        self.row_picks_count[x_index] += 1
        self.column_picks_list[y_index][elem] = True
        self.column_picks_count[y_index] += 1
        self.square_picks_list[square_index][elem] = True
        self.square_picks_count[square_index] += 1

    def get_square_index(self, x_index, y_index):
        """
        Given the intersection of a x-coordinate and a y-coordinate, returns the proper square index
        or raise ModelError(user row-column-square counting) if the arguments are out of range
        """
        if(x_index >= self._rows_size or x_index < 0 or y_index >= self._columns_size or y_index < 0):
            raise ModelError("row or column selection out of range (x:{},y:{})\n".format(x_index + 1, y_index + 1))
        if(x_index < 3):
            return 0 + (y_index >= 3) + (y_index >= 6)
        elif(x_index < 6):
            return 3 + (y_index >= 3) + (y_index >= 6)
        elif(x_index < self._rows_size):
            return 6 + (y_index >= 3) + (y_index >= 6)

    def game_won(self):
        return all(count == 9 for count in self.square_picks_count)
        
if(__name__ == "__main__"):
    # used for testing some methods
    model_test_ob = Board()
    print(model_test_ob.get_square_index(0, 0))
    try:
        print(model_test_ob.get_square_index(0, -1))
    except ModelError as e:
        print(e)
    print(model_test_ob.get_square_index(0, 3))
    print(model_test_ob.get_square_index(0, 6))
    print(model_test_ob.get_square_index(3, 0))
    print(model_test_ob.get_square_index(3, 3))
    print(model_test_ob.get_square_index(3, 6))
    print(model_test_ob.get_square_index(6, 0))
    print(model_test_ob.get_square_index(6, 3))
    print(model_test_ob.get_square_index(6, 6))