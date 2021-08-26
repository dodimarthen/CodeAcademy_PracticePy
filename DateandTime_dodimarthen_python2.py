#DATEANDTIME lesson
#CodeAcademy
#DodiMarthen


#1/6
from datetime import datetime


#2/6
from datetime import datetime

now = datetime.now()
print now.year
print now.month
print now.day
print now


#3/6
from datetime import datetime

now = datetime.now()
print now.year
print now.month
print now.day
print now



#4/6
from datetime import datetime
now = datetime.now()
print '%02d/%02d/%04d' % (now.month, now.day, now.year)



#5/6
from datetime import datetime
now = datetime.now()

print '%02d/%02d/%04d'%(now.month, now.day, now.year) + ' %02d:%02d:%02d' % (now.hour, now.minute, now.second)



#6/6
from datetime import datetime
now = datetime.now()

print '%02d/%02d/%04d'%(now.month, now.day, now.year) + ' %02d:%02d:%02d' % (now.hour, now.minute, now.second)