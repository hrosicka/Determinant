import unittest
import sys
import numpy as np

# setting path
sys.path.append('../DeterminantMatrix')
from determinant import Matrix


class TestMatrix(unittest.TestCase):

    def test_init_square_matrix(self):
        """
        Test that the constructor works for a valid square matrix.
        """
        matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        matrix_object = Matrix(matrix)
        self.assertEqual(matrix_object.matrix.tolist(), matrix.tolist())

    def test_init_non_square_matrix(self):
        """
        Test that the constructor raises an error for a non-square matrix.
        """
        matrix = np.array([[1, 2, 3], [4, 5, 6]])
        with self.assertRaises(ValueError):
            Matrix(matrix)

    def test_init_non_two_dimensional_matrix(self):
        """
        Test that the constructor raises an error for a non-two-dimensional matrix.
        """
        matrix = np.array([1, 2, 3])
        with self.assertRaises(ValueError):
            Matrix(matrix)

    def test_determinant_1x1(self):
        """
        Test determinant calculation for a 1x1 matrix.
        """
        matrix = np.array([[5]])
        matrix_object = Matrix(matrix)
        self.assertEqual(matrix_object.determinant(), 5)

    def test_determinant_2x2(self):
        """
        Test determinant calculation for a 2x2 matrix.
        """
        matrix = np.array([[1, 2], [3, 4]])
        matrix_object = Matrix(matrix)
        self.assertEqual(matrix_object.determinant(), -2)

    def test_determinant_3x3(self):
        """
        Test determinant calculation for a 3x3 matrix.
        """
        matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        matrix_object = Matrix(matrix)
        self.assertEqual(matrix_object.determinant(), 0) 

    def test_determinant_4x4(self):
        """
        Test determinant calculation for a 4x4 matrix.
        """
        matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        matrix_object = Matrix(matrix)
        # Replace with the expected determinant value for the 4x4 matrix
        expected_determinant = 0
        self.assertEqual(matrix_object.determinant(), expected_determinant)
        

if __name__ == "__main__":
  unittest.main()