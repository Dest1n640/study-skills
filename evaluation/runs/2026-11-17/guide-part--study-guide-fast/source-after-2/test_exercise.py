import unittest
from exercise import format_title, parse_numbers, summarize


class ParseTests(unittest.TestCase):
    def test_integers_and_spaces(self):
        self.assertEqual(parse_numbers(" 1, -2, 0 "), [1, -2, 0])

    def test_empty_items(self):
        for text in ["", "1,,2", "1,"]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                parse_numbers(text)

    def test_non_integer(self):
        with self.assertRaises(ValueError):
            parse_numbers("1,2.5")


class SummaryTests(unittest.TestCase):
    def test_values(self):
        self.assertEqual(summarize([1, -2, 4]), {"count": 3, "sum": 3})

    def test_empty(self):
        self.assertEqual(summarize([]), {"count": 0, "sum": 0})


class TitleTests(unittest.TestCase):
    def test_title(self):
        self.assertEqual(format_title("Expenses"), "Report: Expenses")


if __name__ == "__main__":
    unittest.main()

