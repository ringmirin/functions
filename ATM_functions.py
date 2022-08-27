
def atm(pin,balance,ha):
   print("-----welcome to SBI-----")
   print("Please swipe your card:-")
   language=input("Please choose your language: ")
   if language=="english":
      while ha>0:
         pin_code=int(input("Enter four digit pin: ")) 
         
         if pin_code==pin:
            def cash_withdraw():
               withdraw=int(input("Enter your amount: "))
               if withdraw<balance:
                  print("Please collect your money:")
                  print("Remaining balance: ",balance-withdraw)
                  print("Thank you")
               else:
                  print("insufficient amount")
                  print("Please enter less amount")
            def balance_enquiry():
               print("Your current balance is:",balance)
            def diposit():
               cash_diposit=int(input("enter the amount: "))
               print("successfully diposited")
               print("Total balance: ",balance+cash_diposit)
            def main():
               print("1=cash_withdraw")
               print("2=balance_enquiry")
               print("3=diposit")
               user=int(input("Choose your transaction: "))
               if user==1:
                  cash_withdraw()
               elif user==2:
                  balance_enquiry()
               elif user==3:
                  diposit() 
            main()
            print("---Thank you for choosing SBI in your Banking---")
            print(">>>>System Exit<<<<<")
            break
         elif pin_code!=pin:
            print("wrong pin \nTry again")
            ha=ha-1
            if ha==0:
               print("sorry! your card will be block for next 24 hours" ) 
   else:
      print("Sorry!Please choose existing language")
atm(2222,5000,3)
   




