from sys import argv

script_name = argv
prompt = "> "

def name_data(first, last, age, gender):
	print "Your name is %s %s." % (first, last)
	print "You are a(n) %d year old %s." % (age, gender)

print "Welcome to the user identifying program %s.\nWe will now ask a series of questions." % script_name
input_first = raw_input("What is your first name?\n" + str(prompt))
input_last = raw_input("Now, what is your last name?\n" + str(prompt))
input_age = int(raw_input("Please tell us your age.\n" + str(prompt)))
input_gender = raw_input("What is your gender?\n" + str(prompt))

name_data(input_first, input_last, input_age, input_gender)