def reverse_string(s):
    return s[::-1]


def is_palindrome(s):
    return s == s[::-1]


def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


import unittest


def reverse_string(s):
    return s[::-1]


class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("python"), "nohtyp")
        # Add more test cases here


if __name__ == "__main__":
    unittest.main()

import pytest


def is_palindrome(s):
    return s == s[::-1]


def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    # Add more test cases here


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    # Add more test cases here


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    # Add more test cases here


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    # Add more test cases here
