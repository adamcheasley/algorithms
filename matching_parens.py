"""I like parentheticals (a lot).

"Sometimes (when I nest them (my parentheticals) too much
(like this (and this))) they get confusing."

Write a function that, given a sentence like the one above, along with
the position of an opening parenthesis, finds the corresponding
closing parenthesis.

Example: if the example string above is input with the number 10
(position of the first parenthesis), the output should be 79 (position
of the last parenthesis).
"""

import unittest


def find_closing_paren(instr, start):
    """given the start paren, find its closing paren.
    """
    return 0


class Tests(unittest.TestCase):

    def test_one(self):
        s = ("Sometimes (when I nest them (my parentheticals) too much"
             "(like this (and this))) they get confusing.")
        self.assertEqual(
            find_closing_paren(s, 10), 79)


if __name__ == '__main__':
    unittest.main()
