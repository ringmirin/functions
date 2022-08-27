# Words to Sentence
# Write a function that will create a string from a list of strings , separated by space.
# Input format:
# List contains strings which are separated by commas.
# Constraints:
# String should contain only alphabetical words.
# Output format:
# Returned value must be a sentence in one string with required spaces.

def listofstring(n):
   i=0
   while i<len(n):
      a=" ".join(n)
   
      i+=1
   return a
n=["God","is","loved"]
print(listofstring(n))
 


      

