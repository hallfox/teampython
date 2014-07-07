def break_words(stuff):
    """This function will break up words for us."""#hey pydoc
    words = stuff.split(' ') #hey new string functions
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words) #hey standard lib function

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0) #hey list function
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) #hey reverse indexing
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence) #hey referring to already defined functions
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

#try typing in the command line:
# python -i ex25.py
