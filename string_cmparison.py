# Define a function which takes two arguments(strings) and returns the string with largest length. If both 
# the strings have equal length, print both the strings one below the other.
# Hint :- use len() builtin function..

def comparison(s1,s2):
   if len(s1)>len(s2):
      return(s1)
   elif len(s1)<len(s2):
      return(s2)
   else:
      return(s1,s2)

print(comparison("wel","hello"))