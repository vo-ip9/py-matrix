# py-matrix
A simple implementation of a 2d matrix and many related functions, made entirely in Python. This is mostly for educational purposes, and definitely not as fast/efficient as numpy or eigen.

# The Matrix class
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
- element-wise multiplication: **
