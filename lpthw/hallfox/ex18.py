#dun dun dun functions
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))

#that's a function, here's another one that makes more sense
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))

#one arg this time!
def print_one(arg1):
    print("arg1: %r" % arg1)

#you can even send no arguments!
def print_none():
    print("I got nothin'.")

#and now we call them all
#should be pretty simple after you get the hang of what's going
#on: we name a function, call it with data between the
#parentheses, then capture its output, if it has any
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
