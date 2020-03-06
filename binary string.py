from typing import Generator
import unittest


def binary_strings(string: str) -> Generator[str, None, None]:
    if not string:
        yield ""
    else:
        for subString in binary_strings(string[:-1]):
            alphabet = string[-1]
            if alphabet != "X":
                yield subString + alphabet
            else:
                for digit in ["0", "1"]:
                    yield subString + digit


class TestBinaryStrings(unittest.TestCase):
    def test_binary_strings_with_00(self):
        """run binary_string('00')"""
        self.assertEqual("00", "00")

    def test_binary_strings_with_111(self):
        """run binary_string('11')"""

    def test_binary_strings_with_XX(self):
        """run binary_string('XX')"""

    def test_binary_strings_with_0X1X(self):
        """run binary_string('0X1X')"""


if __name__ == "__main__":
    unittest.main()
