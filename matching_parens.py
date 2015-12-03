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
    if instr[start] != '(':
        raise KeyError

    stack = 1
    for idx, letter in enumerate(instr[start+1:]):
        if stack == 0:
            return idx + start
        if letter == '(':
            stack += 1
        elif letter == ')':
            stack -= 1

    if stack == 0:
        return idx + start + 1
    return -1


class Tests(unittest.TestCase):

    def test_one(self):
        s = "()"
        self.assertEqual(
            find_closing_paren(s, 0), 1)

        s = "01(34)67"
        self.assertEqual(
            find_closing_paren(s, 2), 5)

        s = ("Sometimes (when I nest them (my parentheticals) too much"
             "(like this (and this))) they get confusing.")
        self.assertEqual(
            find_closing_paren(s, 10), 78)

    def test_closing_not_found(self):
        s = "here a paren: ( that doesn't close"
        self.assertEqual(
            find_closing_paren(s, 14), -1)


if __name__ == '__main__':
    unittest.main()
