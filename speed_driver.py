# Define a function that checks the speed of drivers. This function will take a parameter named speed, 
# and will satisfy the following conditions:
# 1.If speed if less than 70, print 70.
# 2.If speed is more than 70, give 1 point per 5km.(NOTE:This won't count 70).
# 3.If points are more than 12, print “License suspended”


def speed():
   if drive<=70:
      return("70")
   if ((drive-70)/5)>12:
      return("license suspended")
   else:
      return("point:",((drive-70)/5))
drive=int(input("enter the driver speed: "))
print(speed())



