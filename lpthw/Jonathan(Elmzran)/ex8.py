# sets formatter var
formatter = "%r %r %r %r"

# uses the formatter var and runs it through a variet of string formatters, shows flexibility of string formats
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
# a poem
print formatter % (
		"I had this thing.",
		"That you could type up right.",
		"But it didn't sing.",
		"So I said goodnight."
	)