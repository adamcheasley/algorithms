"""
Write an efficient function that checks whether
any permutation of an input string is a palindrome.

I'm assuming here that 'efficient' refers to an algorithm
that runs in O(n) time.

"""
import unittest


def is_permutation_palindromic(instr):
    # if string has even number of chars,
    # all should appear in pairs
    # if string has odd number, we should
    # get all pairs and a singleton.
    # otherwise this is not a palindromic string.
    if len(instr) % 2 == 0:
        #pair up numbers
    else:
        #pair up numbers
        # check we have a singleton
        pass


class Tests(unittest.TestCase):

    def test_all_chars_same(self):
        self.assertTrue(is_permutation_palindromic("aaa"))
        self.assertTrue(is_permutation_palindromic("bbbb"))

    def test_odd_char(self):
        self.assertTrue(is_permutation_palindromic("civic"))
        self.assertTrue(is_permutation_palindromic("ivicc"))
        self.assertFalse(is_permutation_palindromic("civil"))
        self.assertFalse(is_permutation_palindromic("livci"))

    def test_even_chars(self):
        self.assertTrue(is_permutation_palindromic("ciic"))
        self.assertTrue(is_permutation_palindromic("icic"))
        self.assertTrue(is_permutation_palindromic("aa"))
        self.assertFalse(is_permutation_palindromic("oxoo"))


if __name__ == '__main__':
    unittest.main()
