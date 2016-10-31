from sys import argv
script, user_name=argv
prompt='> '
print "Hi %s , Im the  %s script"%(user_name,script)
print "Id like to ask you a few questions?"
print "Do you like me %s?" % user_name
likes=raw_input(promt)
print "Where so yo live %s?" % user_name
lives= raw_input(promt)
print "What kind of computer do you have?"
computer = raw_input(prompt)
print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)
