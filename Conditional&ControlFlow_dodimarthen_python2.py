#CONDITIONAL&CONTROLFLOW
#Python2
#Dodi Marthen

#1/15
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."

        clinic()  

clinic()


#2/15
# Assign True or False as appropriate on the lines below!

print 17 < 328
bool_one = True   # We did this one for you!

print 100 == ( 2 * 50 )
bool_two = True

print 19 <=19
bool_three = True

print -22 >= -18
bool_four = False

print 99 != (98+1)
bool_five = False



#3/15
# Assign True or False as appropriate on the lines below!
dido = (20-10) > 15
print dido
bool_one = False    # We did this one for you!

print (10+17) == 3**16
bool_two = False

print 1**2 <= -1# 1**2 <= -1
bool_three = False

print 40*4 >= -4
# 40 * 4 >= -4
bool_four = True

print 100 != 10**2
# 100 != 10**2
bool_five = False





#4/15
# Create comparative statements as appropriate on the lines below!

# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two = 1000 <= -10

# Make me true!
bool_three = 10.000 != 10**4

# Make me false!
bool_four =  64 < 5

# Make me true!
bool_five = 25 != (5*2) + 5



#5/15
#just click "RUN" and "Next"


#6/15
bool_one = 64 >= 10**2 and 28 == (10 * 1 ) + 7

bool_two = -(-(-(-2))) == -2 and 4 >= 16 ** 0.5

bool_three = 19 % 4 != 300 /10/ 10 and False 


bool_four = -(1**2) < 2 ** 0 and 10 % 10 <= 20 - 10 *2

bool_five = 25 == 5**2 and 100 >= 10**1


#7/15
bool_one = True 

bool_two =  50 == 25*2 or 100 >= 10.000

bool_three = False or False

bool_four = 10 != 10** 0.5 or 100 != 10**2

bool_five =  False or False



#8/15
bool_one = not True

bool_two = True

bool_three = True

bool_four = not 3 ** 2 + 4 ** 2 != 5 ** 2
 
bool_five = not not False



#9/15
bool_one = False or not True and True
 
bool_two = False and not True or True

bool_three = True and not (False or False)

bool_four = not not True or False and not True

bool_five = False or not (True and True)



#10/15
# Use boolean expressions as appropriate on the lines below!

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = not False

# Make me false!
bool_three = False or False

# Make me true!
bool_four = True and True

# Make me true!
bool_five = False or True



#11/15
response = "Y"

answer = "Left"
if answer == "Left":
    print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    
# Will the above print statement print to the console?
# Set response to 'Y' if you think so, and 'N' if you think not.




#12/15
def using_control_once():
    if 6 < 8:
        return "Success #1"

def using_control_again():
    if 100 == 10**2 :
        return "Success #2"

print using_control_once()
print using_control_again()



#13/15
answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return False    # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False       # Make sure this returns False
		
		
		
		
#14/15
def greater_less_equal_5(answer):
    if answer > 5 :
        return 1
    elif answer < 5 :          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)





#15/15
def greater_less_equal_5(answer):
    if answer > 5 :
        return 1
    elif answer < 5 :          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)
