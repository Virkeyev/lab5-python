import unittest

from bracket_validator import (
    find_invalid_positions,
    highlight_invalid_brackets,
    validate_brackets,
)


class TestBracketValidator(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(validate_brackets(""))

    def test_text_without_brackets(self):
        self.assertTrue(validate_brackets("Hello, world!"))

    def test_nested_brackets(self):
        self.assertTrue(validate_brackets("<div><p>{ test }</p></div>"))

    def test_all_bracket_types(self):
        self.assertTrue(validate_brackets("({<>})"))

    def test_unclosed_opening_bracket(self):
        self.assertEqual(find_invalid_positions("abc("), [3])
        with self.assertRaisesRegex(ValueError, "позиціях 4"):
            validate_brackets("abc(")

    def test_extra_closing_bracket(self):
        self.assertEqual(find_invalid_positions("abc)"), [3])

    def test_wrong_closing_bracket(self):
        self.assertEqual(find_invalid_positions("(}"), [0, 1])
        with self.assertRaisesRegex(ValueError, "позиціях 1, 2"):
            validate_brackets("(}")

    def test_multiple_invalid_brackets(self):
        self.assertEqual(find_invalid_positions("<div><p>{ test }}</p</div>"), [16, 17])

    def test_visual_highlighting(self):
        self.assertEqual(highlight_invalid_brackets("(}", [0, 1]), "(}\n^^")

    def test_non_string_value(self):
        with self.assertRaises(TypeError):
            validate_brackets(123)


if __name__ == "__main__":
    unittest.main()
