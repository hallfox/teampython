#coincidentally, this is also an exercise in converting
#python 2 code to python 3 for me

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): #missing colon
    """Prints the first word after popping it off."""
    word = words.pop(0) #heh it said 'poop'
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) #missing )
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 5 #this is not five, it is six
print("This should be five: %s" % (five - 1))

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 #used \ instead of /
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) #== instead of = and - instead of _

print("With a starting point of: %d" % start_point)
print("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)) #missing ) during formatting and misspelled 'point'

#sentence = "All god\tthings come to those who weight."
#obviously miscopied, the \t would've added some fun
sentence = "All good things come to those who wait."

#no need to reference the ex25 module, the methods are in this
#file
words = break_words(sentence)
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words) #random . in col 0
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
print(sorted_words) #misspelled 'print'

print_first_and_last(sentence) #misspelled 'first'

print_first_and_last_sorted(sentence) #incorrect indentation and misspelled 'and' and misspelled 'sentence'

