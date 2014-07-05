#new stuff

days = "Mon Tue Wed Thu Fri Sat Sun"
#new concept: escape characters
#these are characters, usually noted by \ that are used to
#signify a different character than what appears to be printed
#here, \n escapes the newline character, the equivalent of
#hitting the enter key
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

#these triple quotes in the context of printing signify an
#as-is printing style, ie what you see in your editor is how
#the text will be printed
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
""")

"""Triple quotes can also be used as a form of multiline
commenting and will later be used for an easy documentation."""
