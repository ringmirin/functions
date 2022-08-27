
question=["who is the the health cordinator?","who is the FC?","who is the IT?","who is the T&p?"]
option_list=[["Bhavana","Ringphuliu","Narani","Kamala"],
            ["Seminao","Katimla","Likita","Sarika"],
            ["Nikita","Grace","Anshika","Swathi"],
            ["Anesha","Pretty","Pooja","Manori"]]
ans=[2,4,1,4]
live=[["Bhavana","Ringphuliu"],["Likita","Sarika"],["nikita","Grace"],["Pooja","Manori"]]
live_line=[2,2,1,3]
count=0
def fifty_fifty(i):
   global count
   a=0
   if count==0:
         while a<len(live[i]):
            print(a+1,live[i][a])
            a+=1
         user1=int(input("enter your ans: "))
         count+=1
         if user1==live_line[i]:
               return True
         else:
            return False
            
   else:
         print("you have already used live line ")
         return "y"
def option(i):
      b=0
      while b<len(option_list[i]):
         print(b+1,option_list[i][b])
         b+=1
      user2=int(input("enter you ans: "))
      if user2==ans[i]:
         return True
      elif user2==5050:
         return fifty_fifty(i)
      else:
         return False
def question_list():
      i=0
      while i<len(question):
         print("Q",i+1,question[i])
         x=option(i)
         if x==True:
            print("Congratulation")
         elif x=="y":
            i-=1
         else:
            print("game over")
            break
         i+=1
question_list()

   
