from sys import argv #enter script name, from file, and to file
from os.path import exists

script, from_file, to_file= argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line too, how?
# in_file = open(from_file)
# indata=in_file.read()
indata=open(from_file).read()

print "The input file is %d bytes long" % len(indata) #len gives size of file

# print "Does the output file exist? %r" % exists(to_file) #exists returns true or false depending on whether file actually exists
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input() #prompts on a blank line

out_file = open(to_file,'w') #opens to file for writing
out_file.write(indata) #writes read data from from_file

print "Alright, all done."

out_file.close()
open(from_file).close()
