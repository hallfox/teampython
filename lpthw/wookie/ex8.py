#sets variable formatter to 4 %r formatters
# %r is for debugging
formatter = "%r %r %r %r"

#prints 1 2 3 4
print formatter % (1, 2, 3, 4)
#prints the strings 1 2 3 4
print formatter % ("one", "two", "three", "four")
#prints 4 boolean values t f t f
print formatter % (True, False, True, False)
#prints formatter 4 times consisting of the %r formatters
print formatter % (formatter, formatter, formatter, formatter)
#I still don't understand why it used single quotes and double quotes
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

#misspelled formatter once as foramtter