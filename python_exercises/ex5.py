name ="Ksenia"
age=23
height=163#cm
inches_height=163/2.54
weight=52#kilo
lbs_weight=52*2.2
eyes='Green'
hair='Brown'

print "My name is %s." % name
print "My height %d cm and %d inches tall." % (height,inches_height)
print "My weight %d kilos and  %d lbs." % (weight,lbs_weight)
print "My %s eyes and %s hair." % (eyes, hair)

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
