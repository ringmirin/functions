# Create a funciton named eligibleforvote which tell the user if he/she is eligible to vote or not.
# ( Consider minimum age of voting to be 18. )

def eligibleforvote():
   if user>=18:
      return("Eligible for Voting")
   else:
      return("Not eligible for voting")
user=int(input("Enter the age: "))
print(eligibleforvote()) 


