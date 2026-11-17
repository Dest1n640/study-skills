import unittest
from exercise import count_positive


class CountTests(unittest.TestCase):
    def test_excludes_zero(self):
        self.assertEqual(count_positive([-2, 0, 3]), 1)

    def test_empty(self):
        self.assertEqual(count_positive([]), 0)

    def test_positive_values(self):
        self.assertEqual(count_positive([1, 2, 3]), 3)


if __name__ == "__main__":
    unittest.main()

