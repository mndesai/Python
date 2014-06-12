# print "How old are you?",
# age= raw_input()
# print "How tall are you?",
# height=raw_input()
# print "How much do you weight?",
# weight=raw_input()

# print "So, you're %r old, %r tall and %r heavy." %(age,height,weight)

#raw_input takes an argument and returns it as a string

print "What length would you like to convert from inches to cm?"
in_lnt=int(raw_input())
print "%din is equivalent to %.2f in cm." %(in_lnt, in_lnt*2.54) #this doesn't work because the length is inputted as a string, but we need it as a float