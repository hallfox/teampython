def setup():
    """ Just returns the player's name. Is there anything else we might need
    in the beginning? """
    return prompt("What is your name?")

def safe(usstr):
    """ Just a way to format strings to protect humans
    from their own stupidity. """
    return usstr.strip().lower()

def intro(name):
    """ The premise of the game goes here. """
    print("\nWelcome, %s, to the Star Ship Liberty." % name)

def prompt(message):
    """ A simple function for automating asking the player for input. """
    print("\n%s" % message)
    return input("> ")

def respond(uscmd):
    scmd = safe(uscmd)
    #remember to handle a command here and call it
    if scmd == "look":
        look()
    elif scmd == "help":
        man()
    elif scmd == "quit":
        q = stop()
        if q:
            print("\nGoodbye.")
            return False
    else:
        print("\nI am unsure how to '%s.'" % scmd)
    return True

#all commands go here
def look():
    """ Provides a description of the room. """
    print("\nIt's the cafeteria of the S.S. Liberty. Oddly, it's completely vacant of all life.")

def man():
    """ Lists valid commands. Add yours if you add any. """
    print("\nValid commands: look, help, quit")

def stop():
    """ Quits the game. """
    r = safe(input("\nAre you sure you want to quit? (y/n) "))
    return r == 'y'


name = setup()
intro(name)

#stories below here
def hallfox_story(name):
    go = True
    while go:  #see while loops, Ex 33
        uscmd = prompt("What will you do?")
        go = respond(uscmd)


#start your story here
hallfox_story(name)
