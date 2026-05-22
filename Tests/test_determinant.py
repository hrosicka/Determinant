# Tests/test_determinant.py
import unittest
import sys
import numpy as np
import os

# Setting path to parent directory to allow direct execution
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from determinant import Matrix


class TestMatrix(unittest.TestCase):

    def test_init_square_matrix(self):
        """Test that the constructor works for a valid square matrix."""
        matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        matrix_object = Matrix(matrix)
        self.assertEqual(matrix_object.matrix.tolist(), matrix.tolist())

    def test_init_non_square_matrix(self):
        """Test that the constructor raises an error for a non-square matrix."""
        matrix = np.array([[1, 2, 3], [4, 5, 6]])
        with self.assertRaises(ValueError):
            Matrix(matrix)

    def test_init_non_two_dimensional_matrix(self):
        """Test that the constructor raises an error for a non-two-dimensional matrix."""
        matrix = np.array([1, 2, 3])
        with self.assertRaises(ValueError):
            Matrix(matrix)

    def test_determinant_1x1(self):
        """Test determinant calculation for a 1x1 matrix."""
        matrix = np.array([[5]])
        matrix_object = Matrix(matrix)
        self.assertAlmostEqual(matrix_object.determinant(), 5, places=5)

    def test_determinant_2x2(self):
        """Test determinant calculation for a 2x2 matrix."""
        matrix = np.array([[1, 2], [3, 4]])
        matrix_object = Matrix(matrix)
        self.assertAlmostEqual(matrix_object.determinant(), -2, places=5)

    def test_determinant_3x3(self):
        """Test determinant calculation for a 3x3 matrix."""
        matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        matrix_object = Matrix(matrix)
        self.assertAlmostEqual(matrix_object.determinant(), 0, places=5)

    def test_determinant_identity_matrix(self):
        """Identity matrix should have determinant 1."""
        matrix = np.eye(5)
        matrix_object = Matrix(matrix)
        self.assertAlmostEqual(matrix_object.determinant(), 1, places=5)

    def test_determinant_with_floats(self):
        """Test determinant calculation with floating point numbers."""
        matrix = np.array([[1.5, 2.5], [3.5, 4.5]])
        matrix_object = Matrix(matrix)
        expected = 1.5 * 4.5 - 2.5 * 3.5
        self.assertAlmostEqual(matrix_object.determinant(), expected, places=5)


if __name__ == "__main__":
    unittest.main()