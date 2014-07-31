# Here's some new strange stuff, remember to type it exactly.

# sets days and months, months are separated with a new line using \n
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# prints days and months after two short strings
print "Here are the days: ", days
print "Here are the months: ", months

# uses triple double quotes to allow for multi-line string printing. Preformatting is the term, I believe
print """
There's something going on here.
With the %r double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""" % days