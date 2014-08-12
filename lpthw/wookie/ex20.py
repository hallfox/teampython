#from sys library import argument variable which 
#lets you put in varaible from commmand prompt or power shell
from sys import argv

#name of script, sets argv to input_file
script, input_file = argv

#function reads file  "(f)" give the function the name "f"
# so you can call it 
def print_all(f):
	print f.read()

# resets reading of file at BYTE 0
def rewind(f):
	f.seek(0)

# function prints lines
def print_a_line(line_count, f):
	print line_count, f.readline()

# current file is variable that is set to open input file
current_file = open(input_file)

#prints file
print "First let's print the whole file:\n"

print_all(current_file)

# rewinds file with seek 0
print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

#set current line
current_line = 1
#prints line (line 1, current file)
print_a_line(current_line, current_file)

#1+1 =2 same thing
current_line = current_line + 1
print_a_line(current_line, current_file)
#2+1 = 3
current_line = current_line + 1
print_a_line(current_line, current_file)

#can make it current_line += 1
# or maybe current_line++