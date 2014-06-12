from sys import argv #open python file with script name and file name

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)." #closes script
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..." #I guess this is what happens if you hit return
target = open(filename, 'w') #can write to file, file contents assigned to target variable

# print "Truncating the file. Goodbye!"
# target.truncate() #tell target to truncate, but truncate doesn't matter if you open with "w"

print "Now I'm going to ask you for three lines." #gets 3 lines from user

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# target.write(line1) #writes new lines to file, each line is its own line
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

target.write("%s\n%s\n%s\n" % (line1, line2, line3)) 
target.close()
target = open(filename)
print target.read()

print "And finally, we close it." #closes file
target.close()

# from sys import argv

# script, filename= argv

# print open(filename).read()
# open(filename).close()
