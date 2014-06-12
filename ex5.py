# name='Zed A. Shaw'
# age=35 #not a lie
# height=74 #inches
# weight=180 #lbs
# eyes='Blue'
# teeth='White'
# hair='Brown'

# print "Let's talk about %s." % name
# print "He's %d inches tall." %height
# print "He's %d pounds heavy." %weight
# print "Actually that's not too heavy."
# print "He's got %s eyes and %s hair." % (eyes, hair)
# print "His teeth are usually %s depending on the coffee." %teeth

# # this line is tricky, try to get it exactly right
# print "If I add %d, %d, and %d I get %d." % (age,weight,height,
# 	age+height+weight)

print "This is a program for converting units."
#inches to centimeters
in2c=2.54
lb2k=.453592

inch_test=4
lb_test=3
print "A length of %d inches is equivalent to %.3f cm." % (inch_test,inch_test*in2c)
print "A weight of %d lbs is equivalent to %.3f kg." % (lb_test,lb_test*lb2k)
#lbs to kilos