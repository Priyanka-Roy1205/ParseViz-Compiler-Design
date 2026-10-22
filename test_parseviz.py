
import unittest
from app import tokenize, build_visualization


class TestParseViz(unittest.TestCase):

    def test_valid_expression(self):
        tokens = tokenize("a+b*c")
        self.assertEqual(tokens, ["a", "+", "b", "*", "c"])

    def test_parentheses(self):
        tokens = tokenize("(a+b)*c")
        self.assertEqual(tokens, ["(", "a", "+", "b", ")", "*", "c"])

    def test_invalid_operator_sequence(self):
        tokens = tokenize("a++b")
        with self.assertRaises(ValueError):
            build_visualization(tokens)

    def test_empty_expression(self):
        with self.assertRaises(ValueError):
            tokenize("")


if __name__ == "__main__":
    unittest.main()
