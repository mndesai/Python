from sys import argv

script, user_name, day=argv
prompt = ':)'

print "Hi %s, I'm the %s script, and it is %s today." % (user_name, script, day)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes=raw_input(prompt)

print "Where do you live %s?" % user_name
lives=raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %s about liking me.
You live in %s. Not sure where that is.
And you have a %s computer. Nice.
""" % (likes, lives, computer)