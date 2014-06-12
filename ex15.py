# from sys import argv

# script, filename = argv #import the file name instead of hard coding it into the program

# txt= open(filename) #assigns text of file to variable "txt"

# print "Here's your file %r:" %filename #prints the name of the file
# print txt.read() #my guess is this prints the text of the file, gives txt a command

# print "Type the filename again:"
# file_again=raw_input(">") #creates a prompt-like symbol

# txt_again=open(file_again)

# print txt_again.read()

filename=raw_input("Enter file name:")
txt=open(filename)
print "Here's your file %r:" % filename
print txt.read()

txt.close()


