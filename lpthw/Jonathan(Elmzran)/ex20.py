# imports arguments
from sys import argv

# sets arguments to variables
script, input_file = argv

# creates print all function, which prints an entire document
def print_all(f):
	print f.read()

# creates a rewind document, which returns the cursor to the beginning of the
# document so it can be read again
def rewind(f):
	f.seek(0)

# creates a function that reads only the next line of a document
def print_a_line(line_count, f):
	print line_count, f.readline(),

# opens the input file, assigns it to current file for manipulation
current_file = open(input_file)

# prints the entire file
print "First let's print the whole file:\n"

print_all(current_file)

# rewinds the file
print "Now let's rewind, kind of like a tape."

rewind(current_file)

# prints each line one at a time. Each time the function is called, the cursor
# is already on the next line, so it simply prints one line each time it is
# called.
print "Let's print three lines:"

# current line is 1
current_line = 1
print_a_line(current_line, current_file)

# current line is now 2
current_line += 1
print_a_line(current_line, current_file)

# current line is finally 3
current_line += 1
print_a_line(current_line, current_file)