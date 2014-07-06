#\t make a tab indention
tabby_cat = "\tI'm tabbed in."
#\n makes a new name
persian_cat = "I'm split\non a line."
#\ backslash allows you to use a character that is normally not allowed
#its called an escape sequence
backslash_cat = "I'm \\ a \\ cat."

#a multiline string using """ and \t to tab and \n for a new line
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
#prints the stuff
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# using single triple quote instead of double quotes
print '''single triple quote!!
ahhhhhhh
SINGLE TRIPLE QUOTE!!\n'''
#double quote
print "Yo, I'm %s tall and I'm testing escape sequences." % "10'2\""
#single quote
print 'Yo, I\'m 4\'2" tall and I\'m testing escape sequences.'
#testing %r  displays EVERYTHING including \ for escape sequence
print "Yo, I'm %r tall and I'm testing escape sequences." % "10'2\""

#makes a whirly thing, kinda cool
print "Lets try this code"
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
		
#study drill
#1 -havent done
#2 ''' takes up less memory?