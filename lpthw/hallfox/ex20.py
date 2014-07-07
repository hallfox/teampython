from sys import argv

script, input_file = argv

def print_all(f):
    #prints the entire contents of the file
    print(f.read())

def rewind(f):
    #goes back to the beginning of the file
    f.seek(0)

def print_a_line(line_count, f):
    #prints the line number (provided you passed the right
    #line number) and then reads the next line from the file
    print(line_count, f.readline())

#open sesame
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1 #uggh so much typing
print_a_line(current_line, current_file)

current_line += 1 #I'm shortcutting here, this works too
print_a_line(current_line, current_file)
