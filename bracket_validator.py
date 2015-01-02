"""
You're working with an intern that keeps coming to you with JavaScript
code that won't run because the braces, brackets, and parentheses are
off. To save you both some time, you decide to write a
braces/brackets/parentheses validator.

Examples:

"{ [ ] ( ) }" should return true
"{ [ ( ] ) }" should return false
"{ [ }" should return false
"""

import unittest


def validate(js):
    """Make sure the opening brackets/parentheses are
    correctly closed.
    """
    openers = ['{', '[', '(']
    closers = ['}', ']', ')']
    open_close_mapping = {
        '}': '{',
        ']': '[',
        ')': '(',
    }
    # create an array of chars
    array = list(js)
    # maintain a stack of openers
    stack = []

    for char in array:
        if char in openers:
            stack.append(char)
        elif char in closers and open_close_mapping[char] != stack[-1]:
            # we are trying to close in the wrong place
            return False
        elif char in closers and open_close_mapping[char] == stack[-1]:
            stack.pop()

    # If everything is closed correctly, we should end up
    # with an empty stack
    return not stack and True or False


class Tests(unittest.TestCase):

    def test1(self):
        self.assertTrue(validate("{ [ ] ( ) }"))

    def test2(self):
        self.assertFalse(validate("{ [ ( ] ) }"))

    def test3(self):
        self.assertFalse(validate("{ [ }"))

    def test4(self):
        self.assertTrue(validate("['hello']"))

    def test5(self):
        self.assertFalse(validate("{['hello']"))


if __name__ == '__main__':
    unittest.main()
