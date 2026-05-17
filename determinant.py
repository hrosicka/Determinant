import numpy as np

class Matrix:
    """
    This class represents a matrix and provides methods for calculating its determinant.
    """
    def __init__(self, matrix):
        """
        Initializes the matrix object.

        Args:
        matrix: A NumPy array or an object that can be converted to a NumPy array.
        """
        # Convert input to a NumPy array with float type to ensure proper behavior and matrix operations
        self.matrix = np.asarray(matrix, dtype=float)

        # Check if the input matrix is two-dimensional (has rows and columns)
        if len(self.matrix.shape) != 2:
            raise ValueError("Matrix must be two-dimensional.")

        # Check if the matrix is square (number of rows equals number of columns)
        if self.matrix.shape[0] != self.matrix.shape[1]:
            raise ValueError("Matrix must be square.")

    def determinant(self):
        """
        Calculates the determinant of the matrix using NumPy's highly optimized 
        algorithm (LAPACK-based LU decomposition). Time complexity: O(n^3).

        Returns:
        Determinant of the matrix (float).
        """
        try:
            # np.linalg.det performs lightning-fast computation even for large matrices
            return float(np.linalg.det(self.matrix))
        except Exception as e:
            raise ValueError(f"Error calculating determinant: {str(e)}")

    def determinant_manual(self):
        """
        Manual implementation using cofactor expansion (for educational purposes).
        Only suitable for small matrices (up to 8x8), otherwise it will cause heavy performance lag.
        
        Returns:
        Determinant of the matrix (float).
        """
        n = self.matrix.shape[0]

        # Base cases for 1x1 and 2x2 matrices
        if n == 1:
            return self.matrix[0, 0]
        elif n == 2:
            return self.matrix[0, 0] * self.matrix[1, 1] - self.matrix[0, 1] * self.matrix[1, 0]

        # Recursive case for matrices larger than 2x2
        else:
            # Safety guard to prevent the application from freezing on 10x10 or larger matrices
            if n > 8:
                raise ValueError("Matrix is too large for manual Laplace expansion. Use determinant() instead.")

            determinant = 0.0
            for i in range(n):
                # Efficient NumPy slicing: remove the 0-th row and the i-th column to create a sub-matrix
                sub_matrix = np.delete(np.delete(self.matrix, 0, axis=0), i, axis=1)

                # Recursive call to find the determinant of the minor
                minor_determinant = Matrix(sub_matrix).determinant_manual()

                # Apply sign and add the cofactor to the total determinant
                determinant += (-1)**i * self.matrix[0, i] * minor_determinant

            return determinant