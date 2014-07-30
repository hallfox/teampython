#ex16
from sys import argv
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the File..."
target = open(filename, 'w')

print "truncating the file. Goodbye!"
target.truncate()

print "Now I'm giong to ask you for three lines."

header ="""
<head>
	<title>Automated Python Web page</title>
</head>
<body bgcolor="orange">

"""

footer = """
</body>
"""
header1 = "<h1>" + raw_input("header 1: ") + " </h1> "
line1 = "<p>" + raw_input("line 1: ") + "</p>"
line2 = "<p>" + raw_input("line 2: ") +  "</p>"
line3 = "<p>" + raw_input("line 3: ") + "</p>"


print "I'm going to write these to the file."

target.write(header + "\n".join( (header1) + line1 + line2 + line3 ) + footer)

print "And finally, we close it."
target.close()