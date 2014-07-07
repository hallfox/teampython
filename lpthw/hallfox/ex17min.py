from sys import argv
with open(argv[2], 'w') as output: output.write(open(argv[1]).read())
