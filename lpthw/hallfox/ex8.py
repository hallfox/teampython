formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    #since we use ' in this string, it will print the string
    #literal with " around it
    "But it didn't sing.",
    "So I said goodnight."
))

#remember you could also do this
formatter = "{} {} {} {}"
print(formatter.format(
    "Roses are #FF0000",
    "Violets are #0000FF",
    "Segmentation fault.",
    "Core dumped."
))
#note the difference here though
#since %r prints the string literal, it also includes the quotes
#around the string
#string.format is equivalent to having a formatter of
# "%s %s %s %s"
