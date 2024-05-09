import numpy as np

class Matrix:
    """
    This class represents a matrix and provides methods for calculating its determinant.
    """
    def __init__(self, matrix):
        """
        Initializes the matrix object.

        Args:
        matrix: A NumPy array representing the matrix.
        """
        # Check if the input matrix is two-dimensional (has rows and columns)
        if len(matrix.shape) != 2:
            raise ValueError("Matrix must be two-dimensional.")
        self.matrix = matrix

        # Check if the matrix is square (number of rows equals number of columns)
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Matrix must be square.")

    def determinant(self):
        """
        Calculates the determinant of the matrix.

        Returns:
        Determinant of the matrix.
        """
        n = self.matrix.shape[0]  # Get the number of rows (and columns for square matrices)

        # Base cases for 1x1 and 2x2 matrices
        if n == 1:
            return self.matrix[0, 0]  # Determinant of a 1x1 matrix is the single element
        elif n == 2:
            return self.matrix[0, 0] * self.matrix[1, 1] - self.matrix[0, 1] * self.matrix[1, 0]  # Determinant of a 2x2 matrix

        # Recursive case for matrices larger than 2x2 (using minor expansion)
        else:
            determinant = 0
            for i in range(len(self.matrix[0])):  # Loop through each column
                # Create sub-matrix excluding the current row and current column
                sub_matrix = np.array([[row[j] for j in range(len(self.matrix[0])) if j != i] for row in self.matrix[1:]])

                # Calculate determinant of the sub-matrix (minor)
                minor_determinant = Matrix(sub_matrix).determinant()

                # Apply sign based on the column index (cofactor expansion)
                determinant += (-1)**i * self.matrix[0][i] * minor_determinant

            return determinant