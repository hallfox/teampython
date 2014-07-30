from sys import argv

script, filename = argv

#here we open a file for reading (default mode is read)
txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())

#extraaaaa creeediiit
this_file = "ex15.py"
pyfile = open(this_file)

print("Here's the code that's running this program!")
print(pyfile.read())

print("I'll also ask you to type it again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

# "It's normal for a programmer to confuse you with their vast
#  extensive knowledge."
# - Zed A. Shaw, Learn Python the Hard Way
#good stuff

#do remember to always close your files always
#VERY IMPORTANT NOT KIDDING
txt.close()
pyfile.close()
txt_again.close()
