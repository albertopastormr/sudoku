from random import randint

class ModelError(Exception):
    """ Wraps exceptions occured at the model for legibility"""

class Cell:

    """
    This class contains the whole logic of a unique Cell
    Attributes:
    value: Integer which contains the current value, it can only be modified once
    """
    def __init__(self, new_value = -1):
        self.value = new_value

    def __str__(self):
        if(self.value is -1):
            return " "
        else:
            return str(self.value + 1)

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
        self.row_picks_list = [[False for i in range(self._rows_size)] for i in range(self._rows_size)]
        self.row_picks_count = [0 for i in range(self._rows_size)]
        self.column_picks_list = [[False for i in range(self._columns_size)] for i in range(self._columns_size)]
        self.column_picks_count = [0 for i in range(self._columns_size)]
        self.square_picks_list = [[False for i in range(self._squares_size)] for i in range(self._squares_size)]
        self.square_picks_count = [0 for i in range(self._squares_size)]
        self._board = [[Cell() for j in range(self._columns_size)] for i in range(self._rows_size)]
        self.init_board()

    def init_board(self):
        num_elems_placed = 0
        num_elems_tried = 0
        while num_elems_placed < self._initial_picks_size and num_elems_tried < self._rows_size * self._columns_size:
            x_index = randint(0, self._rows_size - 1)            
            y_index = randint(0, self._columns_size - 1)
            elem = randint(0, 8)
            try:
                self.place_element(x_index,y_index,elem)
                num_elems_placed += 1
            except:
                pass
            num_elems_tried += 1
                

    def place_element(self, x_index, y_index, elem):
        """
        Place 'elem'(0-8 range) at the intersection x-y received by argument.
        Throws ModelError(user row-column-square counting) if it could not be completed.
        """
        if(self.is_possible_to_place_element(x_index, y_index, elem)):
            square_index = self.get_square_index(x_index,y_index)
            self.row_picks_list[x_index][elem] = True
            self.row_picks_count[x_index] += 1
            self.column_picks_list[y_index][elem] = True
            self.column_picks_count[y_index] += 1
            self.square_picks_list[square_index][elem] = True
            self.square_picks_count[square_index] += 1
            self._board[x_index][y_index].value = elem
            return True
        else:
            return False
    
    def delete_element(self, x_index, y_index):
        """
        Deletes element found at the intersection x-y received by argument.
        Throws ModelError(user row-column-square counting) if it could not be completed.
        """
        if(self.is_possible_to_delete_element(x_index, y_index)):
            elem = self._board[x_index][y_index].value
            square_index = self.get_square_index(x_index,y_index)
            self.row_picks_list[x_index][elem] = False
            self.row_picks_count[x_index] -= 1
            self.column_picks_list[y_index][elem] = False
            self.column_picks_count[y_index] -= 1
            self.square_picks_list[square_index][elem] = False
            self.square_picks_count[square_index] -= 1
            self._board[x_index][y_index].value = -1
            return True
        else:
            return False

    def is_possible_to_place_element(self, x_index, y_index, elem):
        if(x_index >= self._rows_size or x_index < 0 or y_index >= self._columns_size or y_index < 0):
            raise ModelError("row or column selection out of range (x:{},y:{})".format(x_index + 1, y_index + 1))
        if(self._board[x_index][y_index].value is not -1):
            raise ModelError("already an element at row {}, column{})".format(x_index + 1, y_index + 1))
        if(self.row_picks_list[x_index][elem]):
            raise ModelError("element {} already in use in the selected row {}".format(elem + 1, x_index + 1))
        if(self.column_picks_list[y_index][elem]):
            raise ModelError("element {} already in use in the selected column {}".format(elem + 1, y_index + 1))
        square_index = self.get_square_index(x_index,y_index)
        if(self.square_picks_list[square_index][elem]):
            raise ModelError("element {} already in use in the square {}".format(elem + 1, square_index + 1))
        return True

    def is_possible_to_delete_element(self, x_index, y_index):
        if(x_index >= self._rows_size or x_index < 0 or y_index >= self._columns_size or y_index < 0):
            raise ModelError("row or column selection out of range (x:{},y:{})".format(x_index + 1, y_index + 1))
        if(self._board[x_index][y_index].value is -1):
            raise ModelError("empty cell at row {}, column{})".format(x_index + 1, y_index + 1))
        return True

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

    def win(self):
        return all(count == 9 for count in self.square_picks_count)
    
    def lose(self):
        return False

    def __str__(self):
        str_ret = ""
        for i in range(self._columns_size):
            str_ret +=  "   " + str(i + 1) + " " 
        str_ret += "\n " + "_____" * self._rows_size + "\n"
        for i in range(self._rows_size):
            str_ret += str(i + 1)
            for j in range(self._columns_size):
                str_ret += "| " +  str(self._board[i][j]) + " |"
            str_ret += "\n"
        str_ret += " " + "_____" * self._rows_size + "\n"
        return str_ret

class Game():
    """
    Sudoku logic's (model)
    """

    def __init__(self):
        self.board = Board()
    
    def place_element(self, x_index, y_index, elem):
        self.board.place_element(x_index,y_index,elem)
    
    def delete_element(self, x_index, y_index):
        self.board.delete_element(x_index, y_index)
    
    def end(self):
        return self.board.win() or self.board.lose()


class Controller():
    """
    ModelViewController
    Communicates application's view with application's logic (model)
    """

    def __init__(self):
        self.model = Game()

    def execute(self):
        print('Welcome to a new game of Sudoku !\n\nUse row -1 and column -1 to cancel a play')
        while(not self.model.end()):
            print(self.model.board)
            option_selected = int(input('Select your next play:\n1. Place number\n2. Delete number\n0. Exit\n-->'))
            if(option_selected is 1):
                row_selected = int(input('Type the row of your next play [1, 9]-->'))
                column_selected = int(input('Type the column of your next play [1, 9]-->'))
                if(row_selected is not -1 and column_selected is not -1):
                    element_selected = int(input('Type the element of your next play [1, 9]-->'))
                    try:
                        """ Prepares row, column and element for the range used at place_element() [0, 8] """
                        self.model.place_element(row_selected - 1, column_selected - 1, element_selected -1)
                    except ModelError as e:
                        print(e)
            elif(option_selected is 2):
                row_selected = int(input('Type the row of your next play [1, 9]-->'))
                column_selected = int(input('Type the column of your next play [1, 9]-->'))
                if(row_selected is not -1 and column_selected is not -1):
                    try:
                        """ Prepares row and columm for the range used at delete_element() [0, 8] """
                        self.model.delete_element(row_selected - 1, column_selected - 1)
                    except ModelError as e:
                        print(e)
            elif(option_selected is 0):
                print('Exiting the game... Thank you for playing !')
                return
            else:
                print('ERROR: Unknown command')
        
if(__name__ == "__main__"):
    # todo: delete_element() at board and menu() at controller
    control = Controller()
    control.execute() 
    """# used for testing some methods
    model_test_ob = Board()
    # testing some methods
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
    print (model_test_ob)"""