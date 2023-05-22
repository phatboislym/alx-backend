import unittest
index_range = __import__('0-simple_helper_function').index_range


class TestIndexRange(unittest.TestCase):
    def test_index_range(self):
        # Test invalid input values
        self.assertEqual(index_range(-1, 10), (0, 0))
        self.assertEqual(index_range(1, -10), (0, 0))
        self.assertEqual(index_range(-1, -10), (0, 0))
        self.assertEqual(index_range(0, 10), (0, 0))
        self.assertEqual(index_range(1, 0), (0, 0))

        # Test valid input values
        self.assertEqual(index_range(1, 10), (0, 10))
        self.assertEqual(index_range(2, 10), (10, 20))
        self.assertEqual(index_range(3, 10), (20, 30))
        self.assertEqual(index_range(1, 1), (0, 1))
        self.assertEqual(index_range(2, 1), (1, 2))
        self.assertEqual(index_range(1, 7), (0, 7))
        self.assertEqual(index_range(3, 15), (30, 45))


if __name__ == '__main__':
    unittest.main()
