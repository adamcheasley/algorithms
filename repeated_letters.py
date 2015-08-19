"""Write a function where it takes in a string
and words are separated by spaces.
Return the word with the most repeated letters or -1
if there is no word with repeating letters.
"""


def fgr(x):
    gr = ('', -1)
    for word in x.split():
        m = max(map(word.count, word))
        if m > 1 and m > gr[1]:
            gr = (word, m)
    return gr[0] or gr[1]


assert fgr("Today, is the greatest day ever!") == "greatest"
assert fgr("This is a great day") == -1
assert fgr("aaabbb cccc") == "cccc"
