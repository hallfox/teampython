#new escape character, \t = tab
tabby_cat = "\tI'm tabbed in."
#sneaky newline in here
persian_cat = "I'm split\non a line."
#as introduced by Zed, the \\ character so that Python doesn't
#misinterpret \ as a signal for an escape sequence
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#i don't understand what the extra credit is getting at here
#this is perfectly valid code in both Python 2 and 3
#the only reason it might be bad is because some software may
#try "smart quoting" and combing two ' into "
#this is evidenced by the book itself, notice that when he
#refers to triple single quote the text printed in the book is
# "' (double quote, single quote)
print('''Hello ''')

#notice that single quote the escape character get printed
print("%r" % "Sure, that\'s \"wa-ter.\"")
