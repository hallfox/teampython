from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "if you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

#print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1 + str("\n") + line2 + str("\n") + line3)

print "And finally, we close it."
target.close()

print "But wait! There's more!"
target = open(filename)

print "We will now print what we added."
print target.read()

print "Let's print that again! We must first return to the first line, though."
target.seek(0)
print target.read()

print "Now we shall close it."
target.close()

print "Goodbye!"