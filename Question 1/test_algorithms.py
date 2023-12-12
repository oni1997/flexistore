import unittest
import algorithms

class TestFooFunction(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(algorithms.foo([1, 2, 3, 4]),[1])

    def test_negative_integers(self):
        self.assertEqual(algorithms.foo([1, -2, -3, -4]), [1])

    def test_mixed_integers(self):
        self.assertEqual(algorithms.foo([-9, 4, 5, 2, -6, 7, 5, -5]), [2])
        
if __name__ == '__main__':
    unittest.main()
