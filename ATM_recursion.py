def recursion():
   print('>>>>Welcome to SBI ATM<<<<')
   restart=('Y')
   chances = 3
   balance = 5000
   while chances>0:
      pin = int(input('Please Enter You 4 Digit Pin: '))
      if pin == (1234):
         print('You entered your pin Correctly\n')
       
         def option1():
                print('Your Balance is Rs.',balance,'\n')
         
         def option2():
               withdrawl = int(input("enter the amount to withdraw: "))
               if withdrawl<balance:
                  print ('\nYour Balance is now Rs.',balance-withdrawl)
               elif withdrawl>balance:
                  print('Invalid Amount, Please Re-try\n')
                  restart
    
         def option3():
               pay_in = int(input('enter the amount to diposit: '))
               print(pay_in+balance)
               print ('\nYour Balance is now Rs.',balance)

         def main():
            print('1 For Your Balance')
            print('2 To Make a Withdrawl')
            print('3 To diposit')
            option=int(input("choose your transaction: "))
            if option==1:
               option1()
            elif option==2:
               option2()
            elif option==3:
               option3()
         main()
         restart=input("would you like to continue?")
         if restart in("n","no"):
            print("\nThank you, for Banking with us!...")
            break
   
      elif pin != ('1234'):
        print('Incorrect Password')
        chances=chances-1
        if chances==0:
            print('card limit exit \nYour card will be block for 24 hours')
            break
   print("\n---System Existing---")
recursion()