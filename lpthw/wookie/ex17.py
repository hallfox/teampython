from sys import argv;from os.path import exists;script, from_file, to_file = argv;print "Copying from %s to %s" % (from_file, to_file);in_file = open(from_file); indata = in_file.read();print "The input file is %d bytes long" % len(indata);print "Does the output file exist? %r" % exists(to_file);print "Ready, hit return to continue, CTRL-C to abort.";raw_input();out_file = open(to_file, 'w');out_file.write(indata);print "Alright, all done.";out_file.close();in_file.close();

#output.close() was necessary because some implementations of python do not always close a file
#https://mail.python.org/pipermail/tutor/2012-January/088031.html
#"Second, some operating system platforms won't let the same file be 
#simultaneously open for readonly and for write.  So if the two filenames 
#happened to be the same file (through symlink or other mechanism, or 
#even using two different ways to describe the same file), you might get 
#an error trying to write without having closed the input file.