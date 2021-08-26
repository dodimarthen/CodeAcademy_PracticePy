#CodeAcademy python 2 #STRING & CONSOLE OUTPUT
#1/16

brian = "Hello life!"

#2/16
# Assign your variables below, each on its own line!
caesar = "Graham"
praline = "John"
viking = "Teresa"


# Put your variables above this line

print caesar
print praline
print viking


#3/16
# The string below is broken. Fix it using the escape backslash!

'This isn\'t flying, this is falling with style!'


#4/16
"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""

fifth_letter = "MONTY"[4]

print fifth_letter


#5/16
parrot = "Norwegian Blue"
print len(parrot)


#6/16
parrot = "Norwegian Blue"

print parrot.lower()


#7/16
parrot = "norwegian blue"

print parrot.upper()


#8/16
"""Declare and assign your variable on line 4,
then call your method on line 5!"""

pi = 3.14
print str(pi)


#9/16
ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()

#10/16
"""Tell Python to print "Monty Python"
to the console on line 4!"""
name = "Monty Python"
print name


#11/16
"""Assign the string "Ping!" to
the variable the_machine_goes on
line 5, then print it out on line 6!"""

the_machine_goes = "Ping!"
print the_machine_goes


#12/16
# Print the concatenation of "Spam and eggs" on line 3!

print "Spam " + "and" + " eggs"


#13/16
# Turn 3.14 into a string on line 3!

print "The value of pi is around " + str(3.14)


#14/16
string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)
#Just hit the "RUN" button


#15/16
name = "Alex"
quest = "Teaching Python"
color = "Blue"

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s" % (name, quest, color)



#16/16
# Write your code below, starting on line 3!

my_string = "Hey, I'm learning python 2"
print len(my_string)
print my_string.upper()