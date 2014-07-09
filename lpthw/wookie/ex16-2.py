from sys import argv

script, file = argv

txt = open(file)

print "Here is the file %s" % file
print txt.read()