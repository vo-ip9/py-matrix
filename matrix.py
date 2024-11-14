"""import random to create pseudo-random matrix elements"""
from random import randint

class Matrix():
    """**A basic 2-dimensional matrix class.**

       Matrix data is stored in a single Python list in a row-major format,
       along with the number of rows and columns. This is a much more efficient
       design than a list of lists, in terms of both memory usage and execution time.
       
       **Attributes**
       - number of rows: int
       - number of columns: int
       - matrix data: list[int | float | str]
       
       **Methods**
       - get_index()
       - get_element()
       - remove_column()
       - remove_row()
       - is_square()
       - dimensions()
       - print_matrix()
       - get_max_element_length()
       - get_submatrix()
       - determinant()
       
       **Built-in matrix operators**
       - is equal to: ==
       - is not equal to: !=
       - addition: +
       - subtraction: -
       - normal multiplication (matrix or scalar): *
       - element-wise multiplication: **"""

    def __init__(self: object, rows: int, cols: int, mdata: list[int]) -> None:
        if rows * cols == len(mdata):
            self.rows = rows
            self.cols = cols
            self.mdata = mdata
        else:
            raise ValueError("Number of rows and/or columns do not match the data given.")


    def __eq__(self, m2: object) -> bool:
        return self.mdata == m2.mdata


    def __ne__(self, m2: object) -> bool:
        return not self.mdata == m2.mdata


    def __add__(self: object, m2: object) -> object | None:
        """returns a matrix-matrix sum of the given matrixes."""
        if self.dimensions() == m2.dimensions():
            return Matrix(self.rows, self.cols, [i+j for i, j, in zip(self.mdata, m2.mdata)])
        raise ValueError("Matrix dimensions must be equal to add.")


    def __mul__(self: object, fact: object | int | float) -> object | None:
        """returns the matrix-scalar or matrix-matrix product of the given factors."""
        if isinstance(fact, int | float): # matrix-scalar multiplication
            return Matrix(self.rows, self.cols, [i*fact for i in self.mdata])
        if isinstance(fact, Matrix): # matrix-matrix multiplication
            if self.cols == fact.rows:
                res = []
                for i in range(self.rows):
                    for j in range(fact.cols):
                        sum_ = 0
                        for k in range(self.cols):
                            sum_ += self.get_element(i, k) * self.get_element(k, j)
                        res.append(sum_)
                return Matrix(self.rows, fact.cols, res)
            raise ValueError("Columns of matrix 1 and rows of matrix 2 must be equal to multiply.")


    def __sub__(self: object, m2: object):
        """returns a matrix-matrix difference of the given matrixes."""
        if self.dimensions() == m2.dimensions():
            return Matrix(self.rows, self.cols, [i-j for i, j, in zip(self.mdata, m2.mdata)])
        raise ValueError("Matrix dimensions must be equal to subtract.")


    def __pow__(self: object, m2: object):
        """returns the element-wise product of the given matrixes"""
        if self.dimensions() == m2.dimensions():
            return Matrix(self.rows, self.cols, [i*j for i, j, in zip(self.mdata, m2.mdata)])
        raise ValueError("Matrix dimensions must be equal to (symmetrically) multiply.")


    def get_index(self: object, row: int, col: int) -> int:
        """returns the 1-dimensional (list) index of a 2-dimensional (row and column) index."""
        return row * self.cols + col


    def get_element(self: object, row: int, col: int) -> int:
        """returns the element at the given (row and column) index."""
        return self.mdata[self.get_index(row, col)]


    def remove_column(self: object, index: int) -> None:
        """removes the specified column from the matrix and changes the dimensions."""
        for row in range(self.rows-1, -1, -1):
            self.mdata.pop(self.get_index(row, index))
        self.cols -= 1


    def remove_row(self: object, index: int) -> None:
        """removes the specified row from the matrix and changes the dimensions."""
        for column in range(self.cols-1, -1, -1):
            self.mdata.pop(self.get_index(index, column))
        self.rows -= 1


    # TODO: add_column(), add_row() implementation


    def is_square(self: object) -> bool:
        """returns a boolean identifying if the matrix is square or not, 
        i.e. a matrix whose number of rows are equal to number of columns."""
        return self.rows == self.cols


    def dimensions(self: object) -> bool:
        """returns a tuple containing the number of rows and columns, respectively."""
        return (self.rows, self.cols)


    def random_matrix(self, rows: int = 3, columns: int = 3, range_: tuple = (0,1)) -> object:
        """returns a matrix with pseudo-random elements in the specified 
        range (inclusive), with the specified number of rows and columns."""
        return Matrix(rows, columns, [randint(range_[0], range_[1]) for _ in range(rows*columns)])


    def get_sub_matrix(self: object, column: int) -> object:
        """helper function used in the determinant function. Returns a square
        submatrix by removing the first row and the specified column."""
        mx = self.copy_matrix()
        mx.remove_row(0)
        mx.remove_column(column)
        return mx


    def determinant(self: object) -> int:
        """returns the determinant of the given matrix. Must be square.\n
        WARNING: This has a time-complexity of O(n!), so don't even try 
        it with a matrix larger than 10x10 (takes ~60 sec)."""
        if not self.is_square():
            raise ValueError("Matrix must be square to find determinant.")
        if self.rows == 1:
            return self.mdata[0]
        if self.rows == 2:
            return self.mdata[0] * self.mdata[3] - self.mdata[1] * self.mdata[2]

        sign, sum_, col = 1, 0, 0
        while col < self.cols:
            sub_matrix: object = self.get_sub_matrix(col)
            det: int = sub_matrix.determinant()
            sum_ += self.get_element(0, col) * det * sign
            sign *= -1
            col += 1
        return sum_


    def copy_matrix(self: object):
        """returns an exact copy of the given matrix"""
        return Matrix(self.rows, self.cols, list(self.mdata))


    def get_max_element_length(self: object) -> int:
        """returns the length of the longest element in the matrix."""
        return max(len(str(element)) for element in self.mdata)


    def print_matrix(self: object, sep: str = " ", padding: int = 1) -> None:
        """prints a visualisation of the given matrix, with specified padding."""
        max_ = self.get_max_element_length()
        for row in range(self.rows):
            for col in range(self.cols):
                print(str(self.get_element(row, col)) + sep * (max_ -
                    len(str(self.get_element(row, col))) + padding), end="")
            print()
